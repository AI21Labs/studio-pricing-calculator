import requests

from completion_presets import completion_presets

import streamlit as st


API_KEY = st.secrets['api-keys']['ai21-team-prod']


@st.cache
def tokenize(text):
    print("miss")
    resp = requests.post(
        "https://api.ai21.com/studio/v1/tokenize",
        headers={"Authorization": "Bearer " + API_KEY},
        json={
            "text": text,
        }
    )
    return len(resp.json()['tokens'])


# Inject CSS for removing table index and metric widget arrows
hide_table_row_index = """<style>
thead tr th:first-child {display:none}
tbody th {display:none}
</style>
"""
hide_metric_arrow = """<style>
[data-testid="stMetricDelta"] svg {
   display: none;
}
</style>"""
st.markdown(hide_table_row_index, unsafe_allow_html=True)
st.markdown(hide_metric_arrow, unsafe_allow_html=True)


model_fees = {
    'j1-large (7.5B)': {'request': 0.0003, 'generated': 0.03 / 1000},
    'j1-grande (17B)': {'request': 0.0008, 'generated': 0.08 / 1000},
    'j1-jumbo (178B)': {'request': 0.005, 'generated': 0.25 / 1000}
}

st.title('AI21 Studio Pricing Calculator')


complete_tab, rewrite_tab = st.tabs([
    'Complete API',
    'Rewrite API'
])

with complete_tab:
    st.write("""Follow the instructions below to estimate the cost of text generation with AI21 Studio for your use-case. 

Text generation is billed based on the number of requests you perform and the amount of text you generate. Input text is free. Generated text is measured in tokens, where 1 token corresponds to 6 characters of English text on average. 

The calculator computes the number of tokens in a sample of text you provide and produces a monthly cost estimate based on your usage volume.""")

    st.write("""""")


    st.markdown('---')

    st.header('1. Provide example request')

    selected_preset = st.selectbox(
        'Select a preset example to start (you can edit below)',
        completion_presets.keys()
    )
    completion = completion_presets[selected_preset]

    prompt = st.text_area(
        label='Sample prompt',
        value=completion.prompt,
        height=300,
        # max_chars=10000,
    )
    num_prompt_tokens = tokenize(prompt)
    st.caption(f"Your prompt is **{num_prompt_tokens:d} tokens** long. Prompt tokens are free, so the prompt length doesn't affect your costs.")

    sample_completion = st.text_area(
        label='Sample completion',
        value=completion.sample_completion,
        height=100,
        # max_chars=10000,
    )
    num_completion_tokens = tokenize(sample_completion)
    st.caption(f"Your completion is **{num_completion_tokens:d} tokens** long. If you require more than one completion per request, additional completions will count towards the number of generated tokens.")

    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        num_results = st.slider(
            label='# Completions per request',
            value=completion.num_results,
            min_value=1,
            max_value=16,
            step=1
        )
        num_generated_tokens = num_completion_tokens * num_results
    with col2:
        st.metric("# Prompt tokens", num_prompt_tokens, "/request", delta_color="off")
    with col3:
        st.metric("# Generated tokens", num_generated_tokens, "/request", delta_color="off")

    st.markdown("---")
    st.header('2. Estimate Volume')

    col1, col2 = st.columns([3, 2], gap="large")
    with col1:
        st.subheader('Your traffic')
        interval = st.radio(
             label='Interval',
             options=['month', 'day', 'minute'],
             index=0)
        count = st.number_input(
             label=f'# requests per {interval}',
             min_value=1,
             step=1,
             value=1000
        )
        interval2month = {'month': 1, 'day': 30, 'minute': 60 * 24 * 30}
        per_month = count * interval2month[interval]
    with col2:
        st.subheader('Monthly volume')
        st.metric("# Requests", per_month)
        st.metric("# Prompt tokens", per_month * num_prompt_tokens, "FREE")
        st.metric("# Generated tokens", per_month * num_generated_tokens)

    st.markdown("---")

    st.header('3. Calculate cost by model')

    models = list(model_fees.keys())
    request_costs = [model_fees[m]['request'] * per_month for m in models]
    generated_token_costs = [model_fees[m]['generated'] * num_generated_tokens * per_month for m in models]
    total_costs = [x + y for x, y in zip(request_costs, generated_token_costs)]

    columns = st.columns(len(models))
    for col, model, cost in zip(columns, models, total_costs):
        col.metric(model, f"${cost:.2f}", delta='/month', delta_color='off')

    st.caption("Fees vary by the size of the model you choose to use: j1-jumbo is the largest and most capable, j1-large is the smallest and most affordable, with j1-grande somewhere in between.")

    with st.expander('See cost breakdown'):
        st.table(
            {
                'Model Size': models,
                'Requests': [f"${c:.2f}" for c in request_costs],
                'Prompt Tokens': ['FREE' for m in models],
                'Generated Tokens': [f"${c:.2f}" for c in generated_token_costs],
                'Total': [f"${c:.2f}" for c in total_costs]
            }
        )


with rewrite_tab:
    st.write('Coming soon...')
