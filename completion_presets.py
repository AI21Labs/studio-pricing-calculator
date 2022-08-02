from dataclasses import dataclass


@dataclass
class Completion:
    prompt: str
    sample_completion: str
    num_results: int = 1


summarize_restaurant_reviews = Completion(
        prompt="""Summarize the following restaurant review
Restaurant: Luigi's

Review: We were passing through SF on a Thursday afternoon and wanted some Italian food. We passed by a couple places which were packed until finally stopping at Luigi's, mainly because it was a little less crowded and the people seemed to be mostly locals. We ordered the tagliatelle and mozzarella caprese. The tagliatelle were a work of art - the pasta was just right and the tomato sauce with fresh basil was perfect. The caprese was OK but nothing out of the ordinary. Service was slow at first but overall it was fine. Other than that - Luigi's great experience!

Summary: Local spot. Not crowded. Excellent tagliatelle with tomato sauce. Service slow at first.

##

Summarize the following restaurant review
Restaurant: La Taqueria

Review: La Taqueria is a tiny place with 3 long tables inside and 2 small tables outside. The inside is cramped, but the outside is pleasant. Unfortunately, we had to sit inside as all the outside tables were taken. The tacos are delicious and reasonably priced and the salsa is spicy and flavorful. Service was friendly. Aside from the seating, the only thing I didn't like was the lack of parking - we had to walk six blocks to find a spot.

Summary:""",
        sample_completion=""" Great tacos. Very spicy salsa. Cramped inside."""
)


product_description_generator = Completion(
    prompt="""Write product descriptions for fashion eCommerce site based on a list of features.
Product: On Every Spectrum Fit and Flare Dress
Features:
- Designed by Retrolicious
- Stretch cotton fabric
- Side pockets
- Rainbow stripes print
Description: In a bold rainbow-striped print, made up of exceptionally vibrant hues, this outstanding skater dress from Retroliciousis on every spectrum of vintage-inspired style. Made from a stretchy cotton fabric and boasting a round neckline, a sleeveless fitted bodice, and a gathered flare skirt with handy side pockets, this adorable fit-and-flare dress is truly unique and so retro-chic.

##

Write product descriptions for fashion eCommerce site based on a list of features.
Product: Camp Director Crossbody Bag
Features:
- Black canvas purse
- Rainbow space print
- Leather trim
- Two securely-zipped compartments
Description: Take a bit of camp charm with you wherever you go with this black canvas purse! Adorned with a rainbow space motif print, black faux-leather trim, two securely-zipped compartments, and adjustable crossbody strap, this ModCloth-exclusive bag makes sure you command a smile wherever you wander.

##

Write product descriptions for fashion eCommerce site based on a list of features.
Product: Talking Picture Oxford Flat
Features:
- Flat shoes
- Amazing chestnut color
- Man made materials
Description:""",
    sample_completion="""  So many ways to wear this oxford flat - ballet flats, slip-ons, bedazzle 'em - you name the method, we salute your creativity! These wonderful little shoes feature a man-made upper, a rounded almond toe, pleated detailing, and a rubber-sole heel. You can be sure these oxfords will knock about the great indoors as much as they'll hit the road to adventure."""
)

twitter_agent = Completion(
    prompt="""Write a tweet to promote an event for Shmolt, a food and more delivery company.
##
Event: Christmas.
Tweet: Oven broke in the last minute and you have no turkey? No need to panic, with Shmolt delivery it will be at your door step by Christmas eve!
##
Event: Valentine's Day.
Tweet: Order her roses using Shmolt, so you can have time to stop and smell the roses #Valentines
##
Event: Summer Sale.
Tweet: In this heat, why get out of the AC when you have 10% off of all Shmolt deliveries?
##
Event: Mother's Day.""",
    sample_completion="""\nTweet: It's hard being a mom, but finding time to cook is hard. Let us take care of you this Mother's Day with Shmolt!"""
)

instruction_to_sql = Completion(
    prompt="""Create SQL statement from instruction.

Database: Customers(CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country)
Request: all the countries we have customers in without repetitions.
SQL statement:
SELECT DISTINCT Country FROM Customers;

##

Create SQL statement from instruction.

Database: Orders(OrderID, CustomerID, EmployeeID, OrderDate, ShipperID)
Request: select all the orders from customer id 1.
SQL statement:
SELECT * FROM Orders
WHERE CustomerID = 1;

##

Create SQL statement from instruction.

Database: Products(ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
Request: selects all products from categories 1 and 7
SQL statement:
SELECT * FROM Products
WHERE CategoryID = 1 OR CategoryID = 7;

##

Create SQL statement from instruction.

Database: Customers(CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country)
Request: change the first customer's name to Alfred Schmidt who lives in Frankfurt city.
SQL statement:""",
    sample_completion="""\nUPDATE Customers
SET CustomerName = 'Alfred Schmidt'
WHERE CustomerID = 1;

##"""
)

dejargonizer = Completion(
    prompt="""The following sentences contain business jargon. Rewrite them using simple words.

Jargon: The fund managers hope to increase yields by taking on leverage.
Simple: The fund managers hope to get more return on their investments by borrowing money.

Jargon: I need to finish due diligence on this company before I can decide.
Simple: I need to finish background research on this company before I can decide.

Jargon: Can you please get this document over the wall?
Simple: Can you please send this document?

Jargon: Their legal team would like us to open our kimono regarding last year's deals.
Simple:""",
    sample_completion=""" Their legal team would like us to reveal all details of last year's deals."""
)

classify_news_topics = Completion(
    prompt="""Classify the following news article into one of the following topics:
1. World
2. Sports
3. Business
4. Science and Technology
Title:
Astronomers Observe Collision of Galaxies, Formation of Larger
Summary:
An international team of astronomers has obtained the clearest images yet of the merger of two distant clusters of galaxies, calling it one of the most powerful cosmic events ever witnessed.
The topic of this article is:
Science and Technology

===

Classify the following news article into one of the following topics:
1. World
2. Sports
3. Business
4. Science and Technology
Title:
Bomb Explodes Near U.S. Military Convoy (AP)
Summary:
AP - A car bomb exploded early Sunday near a U.S. military convoy on the road leading to Baghdad's airport, Iraqi police said, and a witness said two Humvees were destroyed.
The topic of this article is:
World

===

Classify the following news article into one of the following topics:
1. World
2. Sports
3. Business
4. Science and Technology
Title:
Maradona goes to Cuba
Summary:
The former Argentine football star, Diego Armando Maradona, traveled on Monday to Cuba to continue his treatment against his addiction to drugs.
The topic of this article is:
Sports

===

Classify the following news article into one of the following topics:
1. World
2. Sports
3. Business
4. Science and Technology
Title:
Duke earnings jump in third quarter
Summary:
Duke Energy Corp. reports third-quarter net income of  $389 million, or 41 cents per diluted share, sharply above earnings of  $49 million, or 5 cents per diluted share, in the same period last year.
The topic of this article is:
Business

===

Classify the following news article into one of the following topics:
1. World
2. Sports
3. Business
4. Science and Technology
Title:
D.C. Unveils Stadium Plan
Summary:
Rumors spread that Major League Baseball is edging closer to moving the Expos to Washington as D.C. officials announce plans for a stadium on the Anacostia waterfront.
The topic of this article is:""",
    sample_completion="""\nSports

==="""
)


completion_presets = {
    'Summarize Restaurant Reviews': summarize_restaurant_reviews,
    'Product Description Generator': product_description_generator,
    'Twitter Agent': twitter_agent,
    'Instruction to SQL': instruction_to_sql,
    'De-Jargonizer': dejargonizer,
    'Classify News Topics': classify_news_topics
}