from db import db, January, February, March, April, May, June, July, August, September, October, November, December
from datetime import datetime

db.create_all()
print('Database created succesfully!')
print('Populating database...')

print('Adding January to database...')
tmp = January(
    link='https://www.wfla.com/news/florida/man-shooting-at-target-in-backyard-hits-neighbor-sitting-at-dining-room-table-deputies-say/1682358419',
    headline='Florida Man Shooting at Target in Backyard Hits Neighbor Sitting at Dining Room Table', 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.wcjb.com/content/news/Florida-man-doesnt-get-straw-attacks-McDonalds-employee-503812581.html', 
    headline="Florida man doesn't get straw, attacks McDonald's employee", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.local10.com/news/florida/palm-beach-county/florida-man-arrested-at-mar-a-lago-says-he-came-to-talk-to-trump-about-his-63-trillion', 
    headline="Florida Man Arrested at Mar-a-lago, Says He Came to Talk to Trump About 'His $6.3 Trillion'", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.abcactionnews.com/news/region-pasco/florida-man-arrested-after-hitting-dad-with-pizza-because-he-was-mad-he-helped-birth-him', 
    headline="Florida Man Arrested After Hitting Dad with Pizza Because He Was Mad He Helped Birth Him", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.bradenton.com/news/local/crime/article223972280.html', 
    headline="Florida Man Killed Ex-Girlfriend While Trying to ‘Get Rid of the Devil'", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.inquisitr.com/5238472/florida-man-ferrari-ocean/', 
    headline="Florida Man Intentionally Drove Ferrari 360 Into Ocean At Top Speed", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.local10.com/news/florida/florida-man-denies-syringes-found-in-rectum-are-his', 
    headline="Florida Man Denies Syringes Found in Rectum Are His", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.local10.com/news/florida/florida-man-arrested-after-argument-over-cheesesteak', 
    headline="Florida Man Arrested After Argument Over Cheesesteak", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.wtsp.com/article/news/regional/florida/florida-man-accused-of-burning-son-to-teach-him-lesson-about-fire/67-15a4de8c-d2fb-45be-a35e-a0a073ba33c0', 
    headline="Florida Man Accused of Burning Son to Teach Him Lesson About Fire", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.rollingstone.com/culture/culture-news/shelby-svensen-florida-wife-family-murder-777245/', 
    headline="Florida Man Allegedly Fooled Family Into Believing Murdered Wife Was Still Alive", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://wgno.com/2019/01/11/florida-man-chews-up-police-car-seat-after-cocaine-arrest/', 
    headline="Florida Man Chews Up Police Car Seat After Cocaine Arrest", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.wfla.com/news/florida/florida-driver-finds-boa-constrictor-in-his-car-engine/1699749944', 
    headline="Florida Driver Finds Boa Constrictor in His Car Engine", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.nbc-2.com/story/40121548/shirtless-drunk-florida-man-harasses-people-at-the-park', 
    headline="Drunk, Shirtless Florida Man Harasses People in the Park", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.local10.com/news/florida/florida-man-threatens-to-kill-man-with-kindness-uses-machete-named-kindness', 
    headline="Florida Man Threatens to Kill Man With 'Kindness,' Uses Machete Named 'Kindness'", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://miami.cbslocal.com/2019/01/15/florida-man-causes-crash-steals-truck/', 
    headline="Florida Man Causes Highway Crash, Steals Good Samaritan’s Truck Who Stopped To Help", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.nbc-2.com/story/39799057/man-who-drove-ferrari-into-water-said-jesus-told-him-to', 
    headline="Florida Man Who Drove Ferrari Into Water Said, 'Jesus Told Him To'", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.newsweek.com/florida-man-arthur-leo-proulx-marion-county-police-beers-sexual-advances-1295628', 
    headline="Florida Man Accused of Luring Kids Tells Cops He Can't Recall As He 'Drinks 18-20 Beers' Before Talking to Children", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.myhighplains.com/news/viral-videos/caught-on-cam-horses-chase-suspect-in-florida/1709623786', 
    headline="Caught on Cam: Horses Chase Suspect in Florida", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://patch.com/florida/newportrichey/port-richey-man-accused-throwing-chair-across-steak-n-shake', 
    headline="Port Richey Man Accused Of Throwing Chair Across Steak 'n Shake", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://abc30.com/man-on-vacation-finds-hidden-cameras-in-his-airbnb/5098490/', 
    headline="Man Vacationing in Florida Finds Hidden Cameras in His Airbnb", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='http://www.mysuncoast.com/2019/01/21/florida-man-woman-run-over-by-patrol-car-while-lying-road-watch-eclipse/', 
    headline="Florida Man, Woman Run Over By Patrol Car While Lying in Road to Watch Eclipse", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.wtsp.com/article/news/weird/wtflorida/florida-man-caught-exposing-himself-in-walmart-pillow-aisle-deputies/67-2faaebe2-e403-409d-ae29-3ef65383067c', 
    headline="Florida Man Caught Exposing Himself in Walmart Pillow Aisle", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.nbcmiami.com/news/local/North-Florida-Man-Beats-Pepper-Sprays-Mom-Because-She-Was-a-Narcissist-Police-504741371.html', 
    headline="North Florida Man Beat, Pepper Sprayed Mom Because 'She Was a Narcissist'", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.miamiherald.com/news/state/florida/article225004375.html', 
    headline="‘Trump will handle it.’ Florida Man Has Warning After Harassing Iraqi Neighbors", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.wfla.com/news/florida/man-accused-of-driving-unregistered-atv-running-over-dog/1725305563', 
    headline="Florida Man Driving Unregistered ATV Ran Over Dog", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.thrillist.com/news/nation/florida-man-finds-wwii-grenade-drives-to-taco-bell', 
    headline="Florida Man Finds a WWII Grenade, Places It in His Truck, Drives to Taco Bell", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='', 
    headline="The WWII story was so good that it dominated headlines for a second day. This rare distinction is called 'The Florida Spark.'", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.local10.com/news/florida/florida-man-learns-hard-way-he-stole-laxatives-not-opioids', 
    headline="Florida Man Learns Hard Way He Stole Laxatives, Not Opioids", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.wtsp.com/article/news/weird/wtflorida/florida-man-accused-of-robbing-chinese-restaurant-at-finger-point/67-11cb0cbd-b7b9-4581-8d05-547a873b3744', 
    headline="Florida Man Accused of Robbing Chinese Restaurant at Finger Point", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.wfla.com/news/florida/florida-man-spent-weeks-in-jail-for-heroin-that-was-actually-detergent/1739544148', 
    headline="Florida Man Spent Weeks in Jail for Heroin That Was Actually Detergent", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = January(
    link='https://www.miamiherald.com/news/state/florida/article225336285.html', 
    headline="Florida Man Thought He'd Do Donuts on the Airport Runway. Police Were Not Amused.", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

print("Done adding January!")
print("Adding February to database...")

tmp = February(
    link='https://www.orlandoweekly.com/Blogs/archives/2019/02/01/a-man-actually-punted-a-rabid-coyote-in-kissimmee', 
    headline="A Man Actually Punted a Rabid Coyote in Kissimmee", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='https://www.gainesville.com/news/20190202/man-stabbed-in-back-at-gainesville-bar-over-remark-on-hat', 
    headline="Man Stabbed in the Back at Gainesville Bar Over Remark on a Hat", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='https://www.local10.com/news/florida/wig-helps-lead-to-arrest-of-florida-man-in-7-eleven-robbery-police-say', 
    headline="Wig Helps Lead to Arrest of Florida Man in 7-Eleven Robbery, Deputies Say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='https://www.wtsp.com/article/news/weird/wtflorida/florida-man-attacked-sister-bit-cop-after-someone-touched-his-cigar-police-say/67-4597ad08-bcda-4d13-95f7-d3c94a7983d0', 
    headline="Florida Man Attacked Sister, Bit Cop After Someone Touched His Cigar", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='https://www.wftv.com/news/local/florida-men-accused-of-smearing-feces-in-crunch-fitness-restroom-sauna/915166766', 
    headline="Florida Men Accused of Smearing Feces on Crunch Fitness Bathroom, Sauna", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='https://www.nbc-2.com/story/39917586/florida-man-tried-to-run-over-son-because-he-didnt-want-to-take-a-bath', 
    headline="Florida Man Tried to Run Over Son Because He Didn't Want to Take a Bath", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='https://www.local10.com/news/florida/florida-man-dances-through-dui-sobriety-test', 
    headline="Florida Man Dances Through DUI Sobriety Test", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='https://www.thedrive.com/news/26408/florida-man-gets-stuck-to-prepped-drag-strip-surface-at-the-gt-r-world-cup', 
    headline="Florida Man Gets Stuck to Prepped Drag Strip Surface at the GT-R World Cup", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='https://www.local10.com/news/florida/florida-womans-maternity-photo-includes-alligator-shotgun-bud-light', 
    headline="Florida Woman's Maternity Photo Includes Alligator, Shotgun, Bud Light", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='', 
    headline="A rare day of peace.", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='https://www.wctv.tv/content/news/Florida-man-recorded-himself-having-sex-with-his-dog-deputies-say-505702931.html', 
    headline="Florida Man Recorded Himself Having Sex with Dog", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='https://www.miamiherald.com/news/state/florida/article226168030.html', 
    headline="Florida Man Throws Burrito in Woman’s Face, Cops Say. And This Has Happened Before", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='https://www.inquisitr.com/5295824/florida-man-fights-to-keep-last-809-after-irs-seizes-bogus-980000-tax-refund/', 
    headline="Florida Man Fights To Keep Last $809 After IRS Seizes Bogus $980,000 Tax Refund", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='http://www.wflx.com/2019/02/14/florida-man-caught-camera-licking-doorbell/', 
    headline="Florida Man Caught on Camera Licking Doorbell", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='https://www.golfdigest.com/story/florida-man-claiming-people-were-eating-his-brains-leads-police-on-insane-golf-course-chase', 
    headline="Florida Man Claiming People Were 'Eating His Brains' Leads Police on Insane Golf Course Chase", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='http://news-journalonline.com/news/20190215/man-on-scooter-killed-in-collision-with-deer-on-us-1-in-oak-hill', 
    headline="Man on Scooter Killed in Collision with Deer on U.S. 1 in Oak Hill", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='https://account.miamiherald.com/static/paywall/stop?resume=226415525', 
    headline="Florida Man Charged After Pointing Laser at Helicopter", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='https://www.wthr.com/article/rattlesnake-carrying-florida-man-claims-be-agent-god', 
    headline="Rattlesnake-carrying Florida Man Claims to be 'Agent of God'", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='https://www.wtsp.com/article/news/crime/florida-man-throws-pizza-slice-at-his-mom-during-argument-deputies-say/67-01e8e6f4-f109-4cad-a6a5-6360cd59e343', 
    headline="Florida Man Throws Pizza Slice at Mom During Argument", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='https://www.wfla.com/news/florida/florida-man-fights-off-coyote-with-coffee-cup-i-smashed-him-/1796147044', 
    headline="Florida Man Fights Coyote Off With Coffee Cup: 'I smashed him'", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='https://thetakeout.com/florida-man-arrested-cocaine-lunchables-1832791900', 
    headline="Florida Man Arrested with Cocaine-Stuffed Lunchables", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='https://www.newsweek.com/florida-man-throws-toilet-school-board-window-illinois-1340417', 
    headline="Florida Man Throws Toilet Through School Board Building Window in Illinois, Is Arrested Sitting on Another", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='https://www.wfla.com/news/florida/florida-man-charged-in-death-of-grandma-found-in-maggot-infested-bed/1803776616', 
    headline="Florida Man Charged with Death of Grandma Found in Maggot-Infested Bed", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='', 
    headline="A rare day of peace", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='https://www.foxnews.com/us/florida-man-arrested-for-allegedly-throwing-cookie-at-girlfriend', 
    headline="Florida Man Arrested for Allegedly Throwing Cookie at Girlfriend", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='http://www.brevardtimes.com/2019/02/arrested-florida-couple-pleasure-each-other-in-back-of-cop-car/', 
    headline="Arrested Florida Couple Pleasure Each Other In Back Of Cop Car", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='https://www.wtsp.com/article/news/crime/florida-man-sprayed-other-inmates-with-urine-deputies-say/67-77365ca9-d07f-47f4-9352-f95d9f4b78ef', 
    headline="Florida Man Sprayed Other Inmates with Urine", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='https://www.msn.com/en-us/news/crime/florida-man-who-allegedly-threatened-family-with-coldplay-lyrics-ends-standoff-after-swat-promises-him-pizza/ar-BBUdiNx', 
    headline="Florida Man Who Allegedly Threatened Family with Coldplay Lyrics Ends Standoff After SWAT Promises Him Pizza", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = February(
    link='', 
    headline="A rare day of peace", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

print("February added to database!")
print("Adding March to database...")

tmp = March(
    link='https://www.tampabay.com/florida-politics/buzz/2019/03/01/florida-house-speaker-apologizes-for-referring-to-pregnant-women-as-host-bodies-in-interview-on-abortion/', 
    headline="Florida House Speaker Apologizes for Referring to Pregnant Women as ‘Host Bodies’ in Interview on Abortion", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://gephardtdaily.com/national-international/florida-man-sentenced-to-10-days-for-dragging-shark-behind-boat/', 
    headline="Florida Man Sentenced to 10 Days For Dragging Shark Behind Boat", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.wcjb.com/content/news/Florida-man-rescues-grandma-floating-away-on-ice-throne-506624671.html', 
    headline="Florida Man Rescues Grandma Floating Away on Ice Throne", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.miamiherald.com/news/state/florida/article227090129.html', 
    headline="Florida Man Arrested After Fight About Tupac Shakur", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.miamiherald.com/news/state/florida/article227115444.html', 
    headline="Leaf-burning Florida Man Asks Cop 'Did You Find All My Pot?'", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.orlandoweekly.com/Blogs/archives/2019/03/06/a-florida-man-actually-tried-to-board-a-flight-to-orlando-with-a-fake-grenade', 
    headline="A Florida Man Actually Tried to Board a Flight to Orlando With a Fake Grenade", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.wfla.com/news/florida/florida-man-goes-viral-for-crushing-dance-routine-to-post-malone-song/1834082375', 
    headline="Florida Man Goes Viral for Crushing Dance Routine to Post Malone Song", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.nbcmiami.com/news/local/Central-Florida-Man-Broke-Into-Home-Fell-Asleep-on-Couch-While-High-on-Meth-Police-506869941.html', 
    headline="Central Florida Man Broke Into Home, Fell Asleep on Couch While High on Meth", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.muscalaw.com/blog/2019/march/palm-beach-county-fl-man-arrested-after-fight-over-beachfront-wedding-pictures/', 
    headline="Man Arrested After Fight Over Beachfront Wedding Pictures", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.foxnews.com/food-drink/florida-man-who-attacked-mcdonalds-worker-over-straw-sentenced-to-jail', 
    headline="Florida Man Who Attacked McDonald's Worker Over Straw Sentenced to Jail", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.wtsp.com/article/news/florida-man-accused-of-intentionally-pressure-washing-his-neighbor/67-583fcf3c-4e37-40e8-91f7-346c25d9f416', 
    headline="Florida Man Accused of Intentionally Pressure Washing His Neighbor", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.clickorlando.com/news/florida-man-in-spider-man-mask-steals-bottles-from-liquor-store-deputies-say', 
    headline="Florida Man in Spider-Man Mask Steals Bottles From Liquor Store", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.nbc-2.com/story/40121548/shirtless-drunk-florida-man-harasses-people-at-the-park', 
    headline="Drunk, Shirtless Florida Man Harasses People at the Park", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.pnj.com/story/news/local/2019/03/14/florida-man-hits-pregnant-girlfriend-bag-tortilla-chips-over-babys-paternity-srso-says/3153868002/', 
    headline="Milton Man Hit Pregnant Girlfriend With Bag of Tortilla Chips Over Baby's Paternity", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.wthr.com/article/florida-man-finds-bright-green-iguana-toilet-calls-911', 
    headline="Florida Man Finds Bright Green Iguana in Toilet, Calls 911", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.boston25news.com/news/trending-now/florida-man-breaks-into-store-flips-off-security-camera-deputies-say/931262420', 
    headline="Florida Man Breaks into Store, Flips off Security Camera", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.wdbj7.com/content/news/Florida-man-who-burned-caged-cat-fed-it-to-dogs-gets-no-jail-time-507247941.html', 
    headline="Florida Man Who Burned Caged Cat, Fed it to Dogs Gets No Jail Time", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.wesh.com/article/florida-man-accused-of-throwing-pancake-batter-at-woman-arrested/26857033', 
    headline="Florida Man Accused of Throwing Pancake Batter at Woman Arrested", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.pnj.com/story/news/local/2019/03/19/florida-man-accused-exposing-himself-sammys-dancer/3210196002/', 
    headline="Florida Man Accused of Exposing Himself to Sammy's Exotic Dancer", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.miamiherald.com/news/state/florida/article228166959.html', 
    headline="Squirrel Attacks Florida Man, Rodent Was Raised by Neighbor", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.newsweek.com/florida-man-shoved-woman-because-he-wanted-eat-egg-rolls-her-house-claims-she-1370734', 
    headline="Florida Man Shoved Woman Because He Wanted to Eat Egg Rolls in Her House", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.nbcnews.com/news/us-news/florida-man-googles-self-find-out-which-florida-man-he-n986311', 
    headline="Florida Man Googles Self to Find Out Which Florida Man He Is  ", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.usatoday.com/story/news/politics/2019/03/23/day-after-mueller-report-completed-trump-golfs-kid-rock/3257815002/', 
    headline="Trump Golfs with Kid Rock in Florida, One Day After Mueller Finishes Russia Probe [editor's note: still counts]", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='http://www.brevardtimes.com/2019/03/florida-man-steals-hot-air-balloon-from-indiana-during-florida-man-challenge/', 
    headline="Florida Man Steals Hot Air Balloon From Indiana During Florida Man Challenge", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.wthr.com/article/florida-man-electrocuted-trying-remove-bird-power-line', 
    headline="Florida Man Electrocuted Trying to Remove Bird From Power Line", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.local10.com/news/florida/south-florida-man-calls-cops-after-being-scammed-over-paid-sex', 
    headline="South Florida Man Calls Cops After Being Scammed Over Paid Sex", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.miamiherald.com/news/state/florida/article228487694.html', 
    headline="Florida Man Calls 911 to Get Out of His Fast Food Shift, Cops Say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.usatoday.com/story/news/nation/2019/03/28/florida-man-applied-job-arrested-when-dna-matched-cold-case/3304568002/', 
    headline="A Florida Man's Job Application Led to His Arrest in a 1998 Cold Case", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://people.com/pets/florida-man-shoots-kills-pet-zebra-no-permit/', 
    headline="Florida Man Shoots and Kills Pet Zebra He Did Not Have a Permit For After Animal Escapes", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.wsbtv.com/news/trending-now/florida-man-accused-of-attacking-mom-when-she-wouldnt-dress-his-mannequin/935524590', 
    headline="Florida Man Accused of Attacking Mom When She Wouldn't Dress his Mannequin", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = March(
    link='https://www.wnct.com/news/national/florida-man-arrested-for-stealing-nearly-6-000-worth-of-sunglasses/1890650092', 
    headline="Florida Man Arrested For Stealing Nearly $6,000 Worth of Sunglasses", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

print("March added to database!")
print("Adding April to database...")

tmp = April(
    link='http://www.brevardtimes.com/2018/04/florida-man-catches-cooks-baby-manatee/', 
    headline="Florida Man Catches, Cooks Baby Manatee", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://www.foxnews.com/story/florida-man-who-killed-ex-wife-2-children-called-it-cleansing-act', 
    headline="Florida Man Who Killed Ex-Wife, 2 Children Called It 'Cleansing Act'", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://www.washingtonpost.com/news/dr-gridlock/wp/2018/04/04/florida-man-caught-with-loaded-gun-at-national-airport/?noredirect=on&utm_term=.f666e84627fa', 
    headline="Florida man caught with loaded gun at National Airport", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://www.local10.com/news/florida/florida-man-passes-himself-off-as-decorated-war-veteran-to-land-job-police-say', 
    headline="Florida man passes himself off as decorated war veteran to land job, police say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://wtfflorida.com/news/crime/florida-man-steals-beer-even-though-he-dont-drink-it/', 
    headline="Florida Man Not Really Sure Why He Stole a Pack of Bud Lite", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://www.wfla.com/news/florida/florida-man-accused-of-crushing-live-animals-in-trash-compactor/1104308468', 
    headline="Florida man accused of crushing live animals in trash compactor", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://www.upi.com/Florida-man-sues-to-keep-inflatable-Super-Mario-outside-business/6751491592443/', 
    headline="Florida man sues to keep inflatable Super Mario outside business", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://www.miaminewtimes.com/news/florida-man-arrested-for-serial-gropings-if-you-dont-touch-ass-youre-crazy-8374915', 
    headline="Florida Man Arrested for Serial Gropings: 'If You Don't Touch Ass, You're Crazy'", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://modernconsensus.com/cryptocurrencies/bitcoin/bitcoin-pizza/', 
    headline="Florida man blows 10,000 bitcoin on pizza, Twitter bot keeps reminding us 8 years later", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://www.thedrive.com/news/9138/florida-man-arrested-for-allowing-12-year-old-son-to-crash-car-into-canal', 
    headline="Florida Man Arrested For Allegedly Allowing 12-Year-Old Son to Crash Car into Canal", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://www.nbc4i.com/news/u-s-world/man-says-too-much-music-masturbation-caused-him-to-vandalize-home/1114369111', 
    headline="Florida Man says too much music, masturbation caused him to vandalize home", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://www.marijuana.com/news/2018/04/florida-man-can-grow-his-own-medical-marijuana-judge-rules/', 
    headline="Florida Man Can Grow His Own Medical Marijuana, Judge Rules", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='http://www.nbc-2.com/story/28791019/report-police-impersonator-pulls-over-detectives#.VoHKuMArI1-', 
    headline="Florida Man Impersonating a Police Officer Pulls Over Real Cops", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://jalopnik.com/florida-man-gives-cops-dashcam-footage-that-shows-he-di-1825250291', 
    headline="Florida Man Gives Cops Dashcam Video That Shows He Didn't Cause Wreck But Did Burglarize A Store", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://www.washingtonpost.com/news/local/wp/2015/04/15/a-gyrocopter-just-landed-on-the-capitol-lawn/', 
    headline="Florida Man Lands Gyrocopter on Capitol Lawn to Demand Campaign Finance Reform, Is Arrested", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://www.tampabay.com/news/publicsafety/crime/Florida-man-asks-about-stealing-beer-learns-it-means-jail_167373045', 
    headline="Florida man asks about stealing beer; learns it means jail", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://wtfflorida.com/news/crime/pajama-wearing-florida-man-flirt-waffle-house-waitress-pulls-knife-out/', 
    headline="Pajama-Wearing Florida Man Reportedly Wanted to Flirt with Waffle House Waitress, Pulls a Knife Ou", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='http://foodenvy.tv/florida-man-claims-he-lost-20-pounds-using-something-called-the-chipotle-diet/', 
    headline="Florida man claims he lost 20 pounds using something called the 'Chipotle diet'", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://www.bloomberg.com/news/articles/2018-04-18/florida-man-accused-of-97-million-robocalls-says-he-s-no-kingpin', 
    headline="A Florida Man Has been Accused of Making 97 Million Robocalls", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://www.nydailynews.com/news/national/half-bearded-florida-man-spends-4-20-jail-selling-weed-article-1.2608764', 
    headline="Half-bearded Florida man spends 4/20 in jail for selling marijuana the night before", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://www.al.com/news/2016/04/vanderbilt_law_grad_sues_for_r.html', 
    headline="Florida man sues for right to marry his laptop in same-sex marriage protest", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='http://www.baynews9.com/content/news/baynews9/news/article.html/content/news/articles/bn9/2015/4/21/wimauma_teen_critica.html', 
    headline="Florida Man Bitten By Snake That Friends Say He Enjoyed Kissing", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://www.kentucky.com/news/local/crime/article146272209.html', 
    headline="Florida man accused of sexually abusing young girl is now in Lexington jail", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://www.abcactionnews.com/news/florida-man-slapped-with-big-mouth-billy-bass-singing-fish-after-argument-police-say', 
    headline="Florida man slapped with Big Mouth Billy Bass singing fish after argument, police say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://www.whio.com/news/crime--law/florida-man-steals-woman-panties-leaves-them-porch-with-note/qfAlhreGbPguo3Kq9e3GDJ/', 
    headline="Florida man steals woman's panties, leaves them on porch with note", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://www.orlandoweekly.com/Blogs/archives/2018/04/26/florida-man-arrested-for-kicking-swan-at-lake-eola-while-practicing-karate', 
    headline="Florida man arrested for kicking swans at Lake Eola while practicing karat", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://www.foxnews.com/us/florida-man-71-accused-of-repeatedly-exposing-himself-at-eateries-placed-on-house-arrest', 
    headline="Florida man, 71, accused of repeatedly exposing himself at eateries, placed on house arrest", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://www.apnews.com/26ab77b592f04c939b6f0cf4669d5607', 
    headline="Florida man turns self in weeks after deadly double shooting", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='https://www.nydailynews.com/news/national/fla-man-shoots-wife-home-thinking-burglar-article-1.3962417', 
    headline="Florida man shoots wife after mistaking her for burglar in their home", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = April(
    link='http://www.sun-sentinel.com/news/strange/floriduh-blog/sfl-flduh-meth-surfed-car-20150430-story.html', 
    headline="Florida Man High on Meth Jumps on Strangers' Cars, Surfs Them", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

print("April added to database!")
print("Adding May to database...")

tmp = May(
    link='https://wtfflorida.com/news/crime/after-crashing-his-car-florida-man-asks-trooper-if-he-can-get-more-meth/', 
    headline="After Crashing his Car, Florida Man Asks Trooper if He Can Get More Meth", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='https://boingboing.net/2016/05/02/florida-man-arrested-in-fbi-st.html', 
    headline="Florida man arrested in FBI sting over “weapon of mass destruction” synagogue bombing plans", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='https://www.nbcmiami.com/news/Florida-Man-Who-Told-Cop-He-May-Have-Some-Needles-Between-His-Cheeks-Arrested-on-Drug-Charges-205954401.html', 
    headline="Florida Man Who Told Cop He 'May Have Some Needles Between His Cheeks' Arrested on Drug Charges", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='https://wtfflorida.com/news/crime/florida-man-busted-stealing-dragon-ball-z-action-figures-from-target/', 
    headline="Florida Man Busted Stealing Dragon Ball Z Action Figures from Target", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='http://www.tallahassee.com/story/news/2015/05/13/nearly-nude-man-tased-airport/27246189/', 
    headline="Florida Man Interested in Getting Tased Runs Through Airport in Underwear Waiving Nunchucks", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='https://bossip.com/1311719/florida-man-kills-brother-over-cheeseburger/', 
    headline="Florida Man Kills Brother Over Cheeseburger", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='https://abc7.com/man-tries-to-barbecue-all-the-child-molesters/3436857/', 
    headline="Florida man tries to set motel fire to 'barbecue all the child molesters'", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='https://www.eonline.com/au/news/654876/florida-man-tries-to-cash-368-billion-check-and-then-the-story-gets-really-weird', 
    headline="Florida Man Tries to Cash $368 Billion Check, and Then the Story Gets Really Weird", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='https://wtfflorida.com/news/crime/sheriffs-find-90-pounds-of-panties-in-florida-mans-trailer/', 
    headline="Sheriffs find 90 pounds of panties in Florida man's trailer", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='https://www.nydailynews.com/news/crime/florida-man-arrested-posting-drug-related-selfie-article-1.1787366', 
    headline="Facebook him! Florida man arrested after posting drug-related selfie", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='https://www.fox13memphis.com/news/trending-now/police-florida-man-charged-with-stealing-1-in-robbery/276039238', 
    headline="Florida man charged with stealing $1 in robbery", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='https://www.rt.com/usa/342849-florida-man-gator-arm-cops/', 
    headline="Alligator bites off arm of Florida man trying to flee the cops", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='https://www.huffingtonpost.com.au/2014/05/13/jeremy-bryant-sword-hack-saw-wind-chimes_n_5316297.html', 
    headline="Florida Man Bloodies Ex-Girlfriend With Sword, Hacksaw, Wind Chimes", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='https://wtfflorida.com/news/crime/drunk-florida-man-wakes-up-in-parking-lot-tells-cop-his-name-is-fck-you-sshole/', 
    headline="Drunk Florida Man Wakes Up in Parking Lot, Tells Cop His Name is “F*ck you, *sshole!”", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='http://www.tallahassee.com/story/news/2015/05/13/nearly-nude-man-tased-airport/27246189/', 
    headline="Florida Man Interested in Getting Tased Runs Through Airport in Underwear Waiving Nunchucks", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='http://www.policestateusa.com/2014/howard-bowe/', 
    headline="Florida man and his dog killed by SWAT team during pre-dawn no-knock raid", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='https://www.usatoday.com/story/news/nation-now/2017/05/17/rattlesnake-bites-florida-man-who-tries-kiss/329024001/', 
    headline="Rattlesnake bites Florida man who tries to kiss it", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='https://wtfflorida.com/news/crime/florida-man-drove-through-neighbhors-fence-to-hunt-a-deer/', 
    headline="Florida Man Drove Through Neighbhor's Fence to Shoot a Deer", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='https://www.baynews9.com/fl/tampa/news/2016/5/19/deputies_man_locked_?utm_source=fark&utm_medium=website&utm_content=link', 
    headline="Florida Man locked out of St. Pete Beach hotel room shoots lock", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='https://wtfflorida.com/news/crime/florida-woman-beats-her-florida-man-for-refusing-to-cuddle/', 
    headline="Florida Woman Beats her Florida Man for Refusing to Cuddle in Hot Weather", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='https://m.orlandoweekly.com/Blogs/archives/2018/05/21/florida-man-caught-searching-for-threatened-gopher-tortoises-to-eat', 
    headline="Florida man caught searching for threatened gopher tortoises to eat", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='https://www.winknews.com/2018/05/22/florida-man-climbs-on-playground-equipment-to-tell-children-where-babies-come-from/', 
    headline="Florida man climbs on playground equipment to tell children where babies come from", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='https://www.foxnews.com/us/florida-man-arrested-for-murder-after-pocket-dialing-911', 
    headline="Florida man arrested for murder after pocket dialing 911", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='https://wtfflorida.com/news/crime/drunk-florida-man-pulls-out-knife-and-taser-at-mcdonalds-yells-get-out-of-my-country/', 
    headline="Drunk Florida Man Pulls out Knife and Taser at McDonald's, yells “Get Out of My Country!”", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='http://www.nydailynews.com/news/national/identical-florida-twins-arrested-brick-fight-cops-article-1.2234612', 
    headline="Identical Twin Florida Men Arrested After Getting in Brick Fight", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='https://wtfflorida.com/news/crime/florida-man-attacks-his-mom-with-spaghetti-because-demons-were-in-his-head/', 
    headline="Florida man attacks his mom with spaghetti because “demons were in his head”", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='http://www.tbo.com/news/florida/police-fort-lauderdale-man-stuffed-assault-rifles-down-his-pants-20150527/', 
    headline="Florida Man Arrested for Grand Theft After Trying to Walk Out of Store with AK-47s Stuffed Down His Pants", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='http://www.brevardtimes.com/2018/05/florida-little-caesars-employee-shoots-florida-man-wearing-clown-mask/', 
    headline="Little Caesar's Employee Shoots Florida Man Wearing Clown Mask", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='http://www.theglobeandmail.com/news/world/82-year-old-florida-man-arrested-for-slashing-tires-in-bingo-dispute/article24692142/', 
    headline="82-Year-Old Florida Man Slashes 88-Year-Old Florida Woman's Tires with an Ice Pick for Taking His Seat at Bingo", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='https://wtfflorida.com/news/crime/florida-man-hits-sleeping-roommate-on-head-with-a-skillet-for-being-a-confidential-informant/', 
    headline="Florida Man Hits Sleeping Roommate on Head with a Skillet for Being a “Confidential Informant”", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = May(
    link='', 
    headline="Florida Man charged with attacking minion on Florida boardwalk", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

print("May added to database!")
print("Adding June to database...")

tmp = June(
    link='https://wtfflorida.com/news/crime/florida-man-flees-from-car-crash-crashes-twice-again-cusses-out-good-samaritan-victims/', 
    headline="Florida Man Flees from Car Crash, Crashes Twice Again, Cusses Out Good Samaritan Victims", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://www.cbsnews.com/news/cops-man-arrested-after-being-found-with-decapitated-shark/', 
    headline="Cops: Florida Man arrested after being found with decapitated shark", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://edition.cnn.com/2016/06/03/us/florida-fisherman-rescued/index.html', 
    headline="Florida fisherman rescued after treading water for 20 hours", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='http://www.clickorlando.com/news/florida-man-caught-on-video-dancing-atop-deputys-cruiser_20151106182746944', 
    headline="Florida Man Dances on Top of Police Cruiser to Ward Off Vampires", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://wtfflorida.com/news/crime/florida-man-armed-with-assault-hammer-gets-canned-by-sheriffs-deputy/', 
    headline="Florida Man Armed with Assault Hammer Gets Canned by Sheriff's Deputy", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://wtfflorida.com/news/crime/two-florida-mans-evict-neighbors-using-acid-bombs/', 
    headline="Two Florida Mans Evict Neighbors Using Acid Bombs", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://www.sun-sentinel.com/news/sfl-florida-man-s-body-found-in-alligator-s-mouth-report-says-20160607-story.html', 
    headline="Florida man's body found in alligator's mouth, report says", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='http://www.thesmokinggun.com/documents/bizarre/man-jailed-for-pizza-battery-679035', 
    headline="Florida Man Covered in Pizza Arrested for Pizza Battery After Pizza Dispute", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://globalnews.ca/news/2751663/florida-man-calls-911-to-report-hes-out-of-vodka/', 
    headline="Florida man calls 911 to report he's out of vodka", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://wtfflorida.com/news/crime/old-mean-racist-florida-man-gets-arrested-after-flight-for-harassing-stewardess/', 
    headline="Old, Mean, Racist Florida Man Gets Arrested After Flight for Harassing Stewardess", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://abc7.com/news/man-arrested-after-alleged-assault-with-pizza/776125/', 
    headline="Florida man accused of assaulting roommate with slice of pizza", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://www.yahoo.com/news/blogs/oddnews/florida-man-charged-with-vandalism-after-bumper-sticker-protest-of-judge-who-handled-his-divorce-case-182144393.html', 
    headline="Florida man charged with vandalism after bumper sticker protest of judge who handled his divorce case", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://wtfflorida.com/news/crime/after-a-bad-reaction-florida-man-calls-the-cops-to-complain-about-the-meth-he-bought/', 
    headline="After a “bad reaction,” Florida Man calls the cops to complain about the meth he bought", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://wtfflorida.com/news/crime/florida-man-writes-on-facebook-5-likes-and-ill-go-shoot-up-disney-and-hang-myself/', 
    headline="Florida Man writes on Facebook: “5 likes and I'll go shoot up Disney and hang myself”", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://rollingout.com/2017/06/15/florida-man-arrested-13-year-old-gives-birth-baby/', 
    headline="Florida man arrested after 13-year-old gives birth to his baby", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://www.theledger.com/news/20180616/florida-woman-shoots-estranged-husband-in-testicles-after-he-tries-to-take-her-air-conditioner', 
    headline="Florida woman shoots estranged husband in testicles after he tries to take her air conditioner", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://www.foxnews.com/us/florida-man-arrested-after-dumping-body-by-side-of-the-road-police-say', 
    headline="Florida man arrested after dumping body by side of the road, police say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='http://www.brevardtimes.com/2018/06/video-florida-man-rescues-alligator-from-python-with-bares-hands/', 
    headline="Florida Man Rescues Alligator From Python With Bares Hands", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://www.nydailynews.com/news/national/florida-man-catches-postal-worker-mousetrap-mailbox-article-1.3260152', 
    headline="Florida man sets mousetrap to catch mail-stealing neighbor, snags mail-leaving postal worker instead", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://wtfflorida.com/news/nature/florida-man-pair-dump-gator-wawa/', 
    headline="Florida Man Pair Dump a Gator into Wawa on Friday Night", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://www.grandforksherald.com/news/crime-and-courts/4463284-authorities-arrest-22-year-old-florida-man-connection-rapper', 
    headline="Authorities arrest 22-year-old Florida man in connection with rapper XXXTentacion's shooting death", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='http://www.naplesnews.com/news/crime/collier-man-accused-of-biting-swinging-knife-at-loss-prevention-officer-after-suspected-theft-ep-114-337613241.html', 
    headline="Florida Man Steals Clothes, Bites Security Guard, Flees in Gold Convertible", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://wtfflorida.com/news/crime/florida-man-points-gun-florida-woman-for-texting-while-driving/', 
    headline="Florida Man Points Gun at Florida Woman for Texting While Driving", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://www.bradenton.com/news/local/crime/article213761529.html', 
    headline="The beach swimming area had children. And a guy spearfishing, cops say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://www.pnj.com/story/news/2018/06/25/cape-coral-homeowner-regrets-killing-thousands-honey-bees/731891002/', 
    headline="Florida woman regrets killing thousands of swarming honeybees", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='http://www.brevardtimes.com/2018/06/florida-man-says-he-only-grabbed-his-mother-by-head-to-kiss-her/', 
    headline="Florida Man Says He Only Grabbed His Mother By Head To Kiss Her", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://www.miamiherald.com/news/state/florida/article213902479.html', 
    headline="Naked Florida man stood in a fire and chanted 'gibberish.' Mushrooms did it, cops say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://www.theroot.com/florida-man-captured-on-video-clinging-to-hood-of-speed-1827200038', 
    headline="Florida Man Captured on Video Clinging to Hood of Speeding Car Speaks Out", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://twitter.com/annamphillips/status/615525318858817537?ref_src=twsrc%5Etfw', 
    headline="Judge Tells Florida Man He Must Wear a Plain Bandana in Court", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = June(
    link='https://www.gamespot.com/articles/florida-man-claims-he-invented-iphone-in-1992-sues/1100-6441413/', 
    headline="Florida Man Claims He Invented iPhone in 1992, Sues Apple for $10 Billion", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

print("June added to database!")
print("Adding July to database...")

tmp = July(
    link='https://www.rblandmark.com/News/Articles/7-9-2019/Florida-man-chants-as-police-try-to-arrest-him-%7C-Police-reports-July-1_7/', 
    headline="Florida man chants as police try to arrest him", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://www.nbc-2.com/story/39486840/florida-man-accused-of-putting-semen-in-coworkers-water', 
    headline="Florida man accused of putting semen in coworker's water", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://www.abcactionnews.com/news/state/florida-man-loses-2-fingers-in-fireworks-accident-on-3rd-of-july', 
    headline="Florida man loses 2 fingers in fireworks accident on 3rd of July", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://eu.usatoday.com/story/news/nation-now/2018/07/05/florida-man-celebratory-gunfire-fourth-july-fireworks/759516002/', 
    headline="Florida man hit by celebratory gunfire during Fourth of July fireworks show ", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://www.wctv.tv/content/news/Florida-man-pretending-to-be-a-cop-pulls-over-real-deputy-sheriffs-office-says-512255742.html', 
    headline="Florida man pretending to be a cop pulls over real deputy", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://www.nbcmiami.com/news/local/florida-man-allegedly-stole-pool-floats-from-homes-to-stop-himself-from-raping-women-police/128798/', 
    headline="Florida Man Allegedly Stole Pool Floats From Homes to ‘Stop Himself From Raping Women’", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://www.tampabay.com/news/publicsafety/A-71-year-old-Florida-man-tied-a-gun-to-a-weather-balloon-to-fake-his-own-murder-police-say_170034046/', 
    headline="A 71-year-old Florida man tied a gun to a weather balloon to fake his own murder", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://www.mysuncoast.com/2019/07/08/florida-man-says-lighting-firecrackers-under-childs-bed-is-prank-gone-wrong/', 
    headline="Florida man says lighting firecrackers under child’s bed is a ‘prank gone wrong’", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://www.bradenton.com/news/local/crime/article232487002.html', 
    headline="Florida man runs off to drink a beer after mooning deputies", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://www.nbc-2.com/story/38612239/florida-man-runs-for-his-life-as-neighbor-chases-him-in-tractor', 
    headline="Florida man runs for his life as neighbor chases him in tractor", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()
#july 11th next
tmp = July(
    link='https://www.foxnews.com/us/florida-man-72-tries-to-mow-down-neighbor-with-tractor-during-dispute-cops-say', 
    headline="Florida man, 72, tries to mow down neighbor with tractor during dispute, cops say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://www.reuters.com/article/us-florida-crime/florida-man-with-no-arms-charged-with-stabbing-man-with-scissors-idUSKBN1K131O', 
    headline="Florida man with no arms charged with stabbing man with scissors", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://www.miamiherald.com/latest-news/article213135699.html', 
    headline="Florida man asks cops to test his illegal drugs", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://miami.cbslocal.com/2019/07/14/florida-man-luring-robbery-victims-dating-site/', 
    headline="Florida Man Arrested For Luring Robbery Victims From Dating Site", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://www.foxnews.com/us/florida-man-samurai-sword-wheelbarrow', 
    headline="Florida man arrested, caught on video using samurai sword to fight over wheelbarrow", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://www.foxnews.com/us/florida-man-taser-bystanders-crash', 
    headline="Florida man used Taser to fend off bystanders following crash, police say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://wsvn.com/news/local/florida/deputies-florida-man-tied-up-wifes-lover-cut-off-penis/', 
    headline="Deputies: Florida man tied up wife’s lover, cut off penis", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://www.foxnews.com/us/florida-man-stages-suicide-with-csi-las-vegas-balloon-scheme-to-make-it-appear-as-a-murder-cops-say', 
    headline="Florida man stages suicide with 'CSI: Las Vegas' balloon scheme to make it appear as a murder", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://www.foxnews.com/us/florida-man-33-posed-as-housewife-to-lure-men-into-home-where-hed-secretly-film-sex-acts-for-web-cops-say', 
    headline="lorida man, 33, posed as housewife to lure men into home where he'd secretly film sex acts for web", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://miami.cbslocal.com/2017/07/20/florida-man-bananas-shot-out-utility-workers-tires/', 
    headline="Florida Man Says He Went ‘Bananas,’ Shot Out Utility Workers’ Tires", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://miami.cbslocal.com/2019/07/21/florida-man-arrested-armed-sexual-battery-miami-beach/', 
    headline="Florida Man Arrested For Armed Sexual Battery In Miami Beach", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://www.bbc.com/news/world-us-canada-44917413', 
    headline="Florida gunman who killed man in parking dispute free to go, police say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://www.miamiherald.com/news/state/florida/article233006777.html', 
    headline="Wanted Florida man gives cops his brother’s name — but he was wanted, too",
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://abc13.com/entertainment/florida-man-serves-hot-dogs-to-alligators-from-his-mouth/2247372/', 
    headline="Brave Florida man serves up hot dog lunch for alligators straight from his mouth", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://www.cbsnews.com/news/florida-man-allegedly-stabs-alligator-to-death-tries-to-sell-the-meat/', 
    headline="Florida man allegedly stabs alligator to death, tries to sell the meat", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://www.orlandoweekly.com/Blogs/archives/2017/07/26/florida-man-brandishes-samurai-sword-during-road-rage-incident', 
    headline="Florida man brandishes samurai sword during road-rage incident ", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://www.wwnytv.com/2019/07/27/florida-man-nearly-killed-freak-lawn-furniture-accident/', 
    headline="Florida man nearly killed in freak lawn furniture accident", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://www.nbc-2.com/story/38757824/florida-man-makes-beer-run-with-gator-in-hand', 
    headline="Florida man makes beer run with gator in hand", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://www.wrcbtv.com/story/38371293/florida-man-gets-head-butted-by-alligator', 
    headline="Florida man gets head-butted, knocked out by alligator", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://www.miamiherald.com/news/state/florida/article233288922.html', 
    headline="A Florida man said he was chasing a kitten. But how did his best friend get beaten up?", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='https://www.fox4now.com/news/state/florida-man-hit-by-car-during-failed-in-my-feelings-challenge', 
    headline="Florida man hit by car during failed 'In My Feelings' challenge", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

print("July added to database!")
print("Adding August to database...")

tmp = August(
    link='https://www.country935.ca/2018/08/01/florida-man-carries-live-alligator-liquor-store/', 
    headline="Florida Man carries Live Alligator into Liquor Store", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.wctv.tv/content/news/Florida-man-sentenced-to-life-for-killing-wife-with-hammer-and-knife-513685251.html', 
    headline="Florida man sentenced to life for killing wife with hammer and knife", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.kiro7.com/news/trending-now/florida-man-killed-in-standoff-shot-bb-gun-at-deputies/806179512/', 
    headline="Florida man killed in standoff shot BB gun at deputies", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.nbc-2.com/story/41029728/florida-man-accused-of-grabbing-his-genitals-and-giving-the-finger-to-a-man-and-his-8yearold-son', 
    headline="Florida man accused of grabbing his genitals and giving the finger to a man and his 8-year-old son", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.daytondailynews.com/news/florida-man-arrested-for-attempted-striptease-restaurant/dW4yo3CnfYf0LNcywqFsMM/', 
    headline="Florida man arrested for attempted striptease at restaurant", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.miaminewtimes.com/news/florida-man-on-flakka-thinks-hes-possessed-strips-naked-disrupts-traffic-on-i-95-10616127', 
    headline="Florida Man on Flakka Thinks He's Possessed, Strips Naked, Disrupts Traffic on I-95",
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.foxnews.com/us/florida-man-thc-jesus-returning', 
    headline="Florida man said he smoked THC 'because Jesus was returning,' cops say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.wtxl.com/news/florida-man-shoots-facebook-friend-in-buttocks-after-political-argument/article_743bc0bc-9b61-11e8-80f0-c3846697a632.html', 
    headline="Florida man shoots Facebook friend in buttocks after political argument", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://abc7news.com/police-fla-man-drives-golf-cart-into-walmart-tries-to-run-over-people/5454877/', 
    headline="Police: Florida man drives golf cart into Walmart, attempts to run over people", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.newsweek.com/florida-man-arrested-after-allegedly-forcing-alligator-drink-beer-1463693', 
    headline="Florida Man Arrested After Allegedly Forcing Alligator to Drink Beer", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.orlandoweekly.com/Blogs/archives/2016/08/11/judge-says-florida-man-can-no-longer-order-pizza', 
    headline="Judge says Florida man can no longer order pizza", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.boston25news.com/news/deep-viral/police-florida-man-sprays-women-with-roach-spray-break-out-nunchucks-over-loud-music/976378694/', 
    headline="Florida man sprays women with roach spray, break out nunchucks over loud music, cops say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.10news.com/news/national/florida-man-arrested-for-intentionally-running-over-ducklings-playing-in-a-puddle', 
    headline="Florida man arrested for intentionally running over ducklings playing in a puddle", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://torontosun.com/2017/08/14/florida-man-claiming-to-be-alice-in-wonderland-says-hookah-smoking-caterpillar-told-him-to-destroy-liquor-store-with-forklift-cops/wcm/e906a12c-3391-46db-9924-6f1ff422cf2d', 
    headline="Florida man claiming to be Alice in Wonderland says 'hookah-smoking caterpillar' told him to destroy liquor store with forklift", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://wsvn.com/news/local/florida/police-florida-man-said-hed-bring-gun-to-walmart-if-toy-was-broken/', 
    headline="Police: Florida man said he’d bring gun to Walmart if toy was broken", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.foxnews.com/us/florida-man-arrested-after-chugging-7-bottle-of-wine-in-walmart-bathroom-report', 
    headline="Florida man arrested after chugging $7 bottle of wine in Walmart bathroom: report", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.foxnews.com/us/man-arrested-after-dumping-dirt-on-girlfriends-borrowed-car-with-front-end-loader', 
    headline="Florida man dumped dirt on girlfriend's borrowed car with front-end loader", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.washingtontimes.com/news/2018/aug/18/police-florida-man-88-burns-raccoon-over-eating-ma/', 
    headline="Police: Florida man, 88, burns raccoon over eating mangoes", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.foxnews.com/us/florida-man-shoving-steaks-down-his-pants', 
    headline="Florida man arrested after allegedly shoving steaks worth more than $50 down his pants", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.daytondailynews.com/news/florida-man-accused-biting-toddlers-dozens-times/NRL2JCeSRZOgZCjjiCQ3iN/', 
    headline="Florida man accused of biting 2 toddlers dozens of times", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.telegraph.co.uk/news/2016/08/30/florida-man-vladimir-putin-arrested-on-trespassing-charges/', 
    headline="Florida man Vladimir Putin arrested on trespassing charges", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.theolympian.com/news/weird/article217180515.html', 
    headline="Shirtless Florida man rides motorcycle down highway while lying on his back", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.theledger.com/news/20190329/doctor-florida-man-austin-harrouff-believed-he-was-half-dog-half-man-in-face-biting-double-homicide', 
    headline="octor: Florida man Austin Harrouff believed he was ‘half-dog, half-man’ in face-biting double homicide", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.nbc-2.com/story/38957481/florida-man-threatens-co-worker-with-box-cutter-in-argument-about-christian-music', 
    headline="Florida man threatens co-worker with box cutter in argument about Christian music", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://miami.cbslocal.com/2019/11/07/florida-man-faces-prison-for-sending-threatening-text-messages-about-jews/', 
    headline="Florida Man Faces Prison For Sending Threatening Text Messages About Jews", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.mysuncoast.com/2019/08/26/florida-man-gets-months-prison-after-shooting-himself-while-drinking/', 
    headline="Florida man gets 30 months in prison after shooting himself while drinking", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://eu.usatoday.com/story/news/nation-now/2018/09/07/florida-man-drunk-and-naked-allegedly-set-house-fire/1228241002/', 
    headline="Florida man, drunk and naked, allegedly set house on fire in failed cookie baking attempt ", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.newsweek.com/florida-man-punches-fellow-assisted-living-resident-bathroom-1461211', 
    headline="Florida Man Allegedly Punches Fellow Assisted Living Resident for Taking Too Long in Bathroom", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.thedrive.com/news/23240/florida-man-tells-cop-thats-what-she-said-after-being-pulled-over-and-questioned-about-bulge', 
    headline="Florida Man Tells Cop ‘That’s What She Said’ After Being Pulled Over and Questioned About Bulge", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://www.local10.com/news/2018/08/30/florida-man-arrested-for-giving-girlfriend-a-wet-willy/', 
    headline="Florida man arrested for giving girlfriend a 'wet willy'", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='https://wsvn.com/news/local/florida-man-wins-5000-a-week-for-life-lottery-game/', 
    headline="Florida man wins $5,000 a week for life lottery game", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

print("August added to database!")
print("Adding September to database...")

tmp = September(
    link='https://www.wsbradio.com/news/florida-man-accused-shooting-home-after-woman-leaves-negative-restaurant-review/sPcDDNf3nhs5jIk1GDamwM/', 
    headline="Florida man accused of shooting at home after woman leaves negative restaurant review", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://www.upi.com/Odd_News/2016/09/02/Florida-man-arrested-after-using-wanted-poster-as-Facebook-photo/4241472839032/', 
    headline="Florida man arrested after using wanted poster as Facebook photo", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://www.heraldtribune.com/news/20190903/florida-man-wants-us-military-to-fight-hurricane-dorian-with-ice/1', 
    headline="Florida man wants the U.S. military to fight Hurricane Dorian with ice", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://wsvn.com/news/local/florida-man-parks-smart-car-in-kitchen-so-it-wont-blow-away/', 
    headline="Florida man parks Smart car in kitchen so it won’t blow away", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://miami.cbslocal.com/2018/09/05/florida-man-arrested-200-illegal-lobsters/', 
    headline="Florida Man Caught With Nearly 200 Illegal Lobsters", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://www.independent.co.uk/news/world/americas/florida-man-news-police-escape-abraham-duarte-a8526146.html', 
    headline="Florida man nearly escapes police by jumping into canal — until he swallows algae: 'I'm going to die!'", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://www.abc-7.com/story/39175530/florida-man-tries-to-start-naked-fight-club-at-chickfila', 
    headline="Florida man tries to start naked fight club at Chick-Fil-A", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://www.foxnews.com/us/florida-man-shoots-kills-puppy-from-balcony-during-walk-with-its-owners-police-say', 
    headline="Florida man shoots, kills puppy from balcony during walk with its owners, police say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://www.telegraph.co.uk/news/2017/09/08/florida-gun-owners-encouraged-shoot-storm-fire-guns-hurricane/', 
    headline="Florida gun owners encouraged to 'shoot the storm' and fire their guns at Hurricane Irma ", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://www.orlandoweekly.com/Blogs/archives/2017/09/10/florida-man-gives-brutally-thorough-answer-to-whether-or-not-hes-worried-about-hurricane-irma', 
    headline="Florida man gives brutally thorough answer to whether or not he's worried about Hurricane Irma ", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://www.fox29.com/news/florida-man-spots-firefighter-running-toward-angel-in-clouds-on-september-11', 
    headline="Florida man spots 'firefighter running toward angel' in clouds on September 11", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://www.itv.com/news/2016-09-12/florida-man-shot-dead-after-asking-if-bulletproof-vest-still-worked/', 
    headline="Florida man shot dead after asking if bulletproof vest still worked", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://big1059.iheart.com/content/2018-09-13-florida-man-ends-argument-with-chainsaw-strike/', 
    headline="Florida Man Ends Argument With Chainsaw Strike", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://www.orlandoweekly.com/Blogs/archives/2018/09/14/shirtless-florida-man-travels-to-myrtle-beach-to-head-bang-during-hurricane-florence', 
    headline="Shirtless Florida man travels to Myrtle Beach to head bang during Hurricane Florence ", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://www.heraldtribune.com/zz/news/20190321/police-florida-man-texts-soo-sorry-after-raping-woman', 
    headline="Police: Florida man texts ‘soo sorry’ after raping woman", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://www.cbsnews.com/news/alleged-florida-foot-sniffer-arrested/', 
    headline="Alleged Florida foot sniffer arrested", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://www.wctv.tv/content/news/Florida-man-accused-of-bludgeoning-father-on-boat-receives-nine-year-sentence-560554471.html', 
    headline="Florida man accused of bludgeoning father on boat receives nine year sentence", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://www.miamiherald.com/latest-news/article218627450.html', 
    headline="Florida man rides Sea-Doo on highway", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://wjla.com/news/offbeat/neighbors-complain-about-florida-man-doing-yard-work-naked-police-say-it-is-legal', 
    headline="Neighbors complain about Florida man doing yard work naked, police say it is legal", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://www.mysuncoast.com/2019/09/20/florida-man-gets-probation-picking-up-transporting-turtles/', 
    headline="Florida man gets probation for picking up, transporting 41 turtles", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://www.flyertalk.com/articles/worst-passenger-of-the-week-florida-man-arrested.html', 
    headline=" Florida man was arrested after allegedly attempting to steal a passenger jet", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://theweek.com/speedreads/650409/florida-man-rides-manatee-dares-police-arrest-gets-arrested', 
    headline="Florida man rides manatee, dares police to arrest him, gets arrested", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://www.mysuncoast.com/2019/09/23/smiling-florida-man-faces-th-dui-after-low-speed-chase-deputies-say/', 
    headline="Smiling Florida man faces 5th DUI after low-speed chase, deputies say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://www.wctv.tv/content/news/Naked-Florida-man-chases-couple-around-Chick-fil-A-parking-lot-deputies-say-494163751.html', 
    headline="Naked Florida man chases couple around Chick-fil-A parking lot, deputies say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://www.tampabay.com/news/publicsafety/florida-man-throws-bicycle-then-other-man-off-bridge-20180925/', 
    headline="Florida man throws bicycle, then other man off bridge ", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://eu.usatoday.com/story/news/nation/2019/10/08/florida-man-charged-forcing-captured-alligator-drink-beer/3914220002/', 
    headline="Florida man accused of giving beer to an alligator ", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://abc13.com/florida-man-paralyzed-after-alleged-murder-plot-backfires/5571154/', 
    headline="Florida man paralyzed after alleged murder plot backfires", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://wtkr.com/2018/10/03/florida-man-allegedly-neglected-grandmother-to-point-of-death-buried-her-tried-to-flee-country/', 
    headline="Florida man allegedly neglected grandmother to point of death, buried her, tried to flee country", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://www.engadget.com/2019/10/02/florida-man-cutting-brake-lines/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS91cmw_c2E9dCZyY3Q9aiZxPSZlc3JjPXMmc291cmNlPXdlYiZjZD0yJnZlZD0yYWhVS0V3akl4Y3JhdU5UbkFoVk5pWXNLSFNqTkFsY1FGakFCZWdRSUNoQUYmdXJsPWh0dHBzJTNBJTJGJTJGd3d3LmVuZ2FkZ2V0LmNvbSUyRjIwMTklMkYxMCUyRjAyJTJGZmxvcmlkYS1tYW4tY3V0dGluZy1icmFrZS1saW5lcyUyRiZ1c2c9QU92VmF3M1d1NWFtZV9CWWVBWUMwT19RdnppbQ&guce_referrer_sig=AQAAAAB62kuqxotjnj9o9QRq15z5hApps4N3FN1COLyTtMK95cNMRE2at83O2AEHzwJjzxGeXnc8juVErhL9iJHer31oqqLL2E3IbPrmH5zZyNsrI1DrjQMg8wGay8GTHcPvWd7VG683Okc7ul3X3ElUBMuBRNba31idqbujMbmUtdNf', 
    headline="Florida man arrested for cutting the brake lines of over 100 e-scooters", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='https://www.mysuncoast.com/2019/09/30/florida-man-reunited-with-iphone-more-than-year-after-he-lost-it-ocean/', 
    headline="Florida man reunited with iPhone more than year after he lost it in ocean", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

print("September added to database!")
print("Adding October to database...")

tmp = October(
    link='https://www.wwnytv.com/2019/10/01/florida-man-tried-sell-beer-dolphins-game-police-say/', 
    headline="Florida man tried to sell beer for $724 at Dolphins game, police say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://www.ksla.com/2018/10/02/florida-man-tries-buy-year-old-girl-walmart/', 
    headline="Florida man tries to buy 8-year-old girl at Walmart", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://www.maritimeherald.com/2019/october-9-trending-a-florida-man-is-arrested-for-trying-to-get-a-caiman-drunk-viral-tweet-twitter/', 
    headline="A Florida Man Is Arrested For Trying To Get A Caiman Drunk", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://www.foxnews.com/us/florida-man-claims-he-killed-dismembered-roommate-because-he-was-possibly-next-mass-killer-cops-say', 
    headline="Florida man claims he killed, dismembered roommate because he was possibly ‘next mass killer,’ cops say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://time.com/5416674/florida-kavanaugh-vote-threat/', 
    headline="Florida Man Arrested After Threatening To Kill Politicians Who Vote No on Kavanaugh's Confirmation", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://thecomeback.com/general/florida-man-interrupts-hurricane-matthew-live-tv-report-to-yell-dicks-out-for-harambe.html', 
    headline="Florida Man interrupts Hurricane Matthew live TV report to yell ‘Dicks out for Harambe’", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://www.mysuncoast.com/2019/10/07/police-florida-man-beats-rapes-pregnant-girlfriend-kill-fetus/', 
    headline="Police: Florida man beats, rapes pregnant girlfriend to kill fetus", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://www.foxnews.com/us/florida-suspect-22-allegedly-attacked-mother-with-sausages', 
    headline="Florida suspect, 22, allegedly attacked mother with sausages", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://www.foxnews.com/us/florida-man-shot-outside-bar-after-rejecting-shot-inside-bar-officials-say', 
    headline="Florida man shot outside bar after rejecting shot inside bar, officials say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://www.foxnews.com/us/hurricane-michael-florida-man-writes-name-on-arm-survive', 
    headline="As Hurricane Michael hits, Florida man writes name on arm in case he doesn't survive storm", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/press-releases/october-11-2016-florida-man-pleads-guilty-manufacturing-distributing-performance-enhancing-drugs', 
    headline="Florida Man Pleads Guilty to Manufacturing, Distributing Performance Enhancing Drugs", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://eu.pnj.com/story/news/2018/12/12/naked-florida-man-crossbow-who-claimed-aliens-were-after-him-shot-deputy/2292792002/', 
    headline="Deputy cleared for shooting naked man armed with crossbow who claimed aliens were after him", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://www.winknews.com/2018/10/13/cops-florida-man-hides-heroin-drug-in-5-year-olds-shirt/?__cf_chl_captcha_tk__=feee3ef6cf5bd0245debee3d9a7558ec54592877-1581801600-0-AdK7yMcA7-Dd0qbyP3-ifXhAFen1Dch1WIZudvBsknZojctWRVxUUUEpzRc7jlsSXEXNf7UEFDBLODZ_p5J5G0ZbyWG4nOieOgOh9ij4FiE6kIQTxa8hARQAPOUZt8cFPVTSXdWFO-bj27-Lt6pBN1Ix5J0N5dYLmhYWkNhwYiXEG1alLwjwZEQRRG0XjncLBAj5wc2ADgOdW0GUIDlBUQnTNVfiYRYoaBDF76_4k0elswthXuHDTqsKmHAOD54WcKV3x8mnJp7kuqZQBwVMJ1D9qdGsv8FX5KaFPS85pv4ds4rucKFgdxrB7UvAg9Gmme6gL4mMsDZj2xh_ItuoDrVdLKWea_XY53wlek7qcqRWdgbDfmt2PRNhrHibyeQFr6GOtKnREtqKpUrJklzq-X0', 
    headline="Cops: Florida man hides heroin, drug in 5-year-old’s shirt", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://www.wctv.tv/content/news/Man-run-over-by-lawn-mower-while-trying-to-kill-son-with-chainsaw-497538901.html', 
    headline="Man run over by lawn mower while trying to kill son with chainsaw", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://wsvn.com/news/local/deputies-ask-florida-man-to-quit-calling-about-his-stolen-marijuana/', 
    headline="Deputies ask Florida man to quit calling about his stolen marijuana", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://6abc.com/2540084/', 
    headline="Police: Florida man commits murder over imaginary girlfriend", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://globalnews.ca/news/3013640/florida-man-with-half-a-head-arrested-on-attempted-murder-arson-charges/', 
    headline="Florida man with ‘half a head’ arrested on attempted murder, arson charges", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://www.wptv.com/news/state/police-say-central-florida-man-shot-stranger-because-he-wouldnt-drink-alcohol-with-him', 
    headline="Police say Central Florida man shot stranger because he wouldn't drink alcohol with him", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://www.abcactionnews.com/news/state/florida-man-climbs-up-cellphone-tower', 
    headline="Florida man climbs up cellphone tower", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://www.newsweek.com/florida-man-offered-inmate-money-car-kill-four-people-feed-pigs-alligators-police-say-1475871', 
    headline="Florida Man Offered Inmate $4,000 and a Car to Kill Four People and Feed Them to Pigs and Alligators, Police Say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://www.mysuncoast.com/2019/10/21/florida-man-accused-killing-suspected-peeping-tom/', 
    headline="Florida man accused of killing suspected ‘peeping Tom’", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://cbs12.com/news/local/florida-man-accused-of-having-sex-with-frozen-toy-at-target', 
    headline="Florida man accused of having sex with 'Frozen' toy at Target", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://www.wifr.com/content/news/Florida-woman-hit-man-with-SUV-tried-to-urinate-on-deputy-cops-say-566850031.html', 
    headline="Florida woman hit man with SUV, tried to urinate on deputy, cops say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://www.clickorlando.com/news/2017/10/24/florida-man-stabs-beats-man-with-stick-for-not-giving-him-beer-police-say/', 
    headline="Florida man stabs, beats man with stick for not giving him beer, police say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://www.reuters.com/article/us-usa-packages/florida-man-charged-in-connection-with-14-bombs-sent-to-trump-critics-idUSKCN1MZ1CP', 
    headline="Florida man charged in connection with 14 bombs sent to Trump critics", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://abc3340.com/news/offbeat/report-florida-man-allegedly-slaps-woman-with-a-bowl-of-chili', 
    headline="Florida man allegedly slaps woman with a bowl of chili", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://www.wowt.com/content/news/Florida-man-demands-mug-shot-be-removed-from-Facebook-deputies-replace-it-with-booking-photo-564611021.html', 
    headline="Florida man demands mug shot be removed from Facebook; deputies replace it with booking photo", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://www.upi.com/Odd_News/2019/10/28/Florida-man-jumps-off-surfboard-lands-on-shark/3671572276250/', 
    headline="Florida man jumps off surfboard, lands on shark", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://www.newsweek.com/florida-man-spits-food-womans-mouth-road-rage-1473738', 
    headline="Florida Man Spits Half-Eaten Food into Woman's Mouth During Road Rage Incident, Police Say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://www.inquisitr.com/5139197/florida-man-arrested-for-allegedly-assaulting-girlfriend-while-dressed-as-dinosaur/', 
    headline="Florida Man Arrested For Allegedly Assaulting Girlfriend While Dressed As Dinosaur", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='https://www.clickorlando.com/news/2018/10/31/florida-man-gets-stuck-after-climbing-down-30-foot-well-for-bragging-rights/', 
    headline="Florida man gets stuck after climbing down 30-foot well 'for bragging rights'", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

print("October added to database!")
print("Adding November to database...")

tmp = November(
    link='https://eu.pnj.com/story/news/2018/11/01/pensacola-man-rampages-neighborhood-looking-fight/1849705002/', 
    headline="Pensacola man arrested for barging into homes seeking someone to fight him ", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://newschannel9.com/news/offbeat/florida-man-breaks-into-restaurant-strips-naked-eats-noodles-plays-bongos', 
    headline="Florida man breaks into restaurant, strips naked, eats noodles, plays bongos", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://www.winknews.com/2016/11/03/police-naked-florida-man-drove-with-wires-on-penis/', 
    headline="Police: Naked Florida man drove with wires on penis", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://www.miamiherald.com/news/state/florida/article221538185.html', 
    headline="Florida man dressed like Fred Flintstone pulled over in his ‘footmobile’ ", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://wsvn.com/news/local/florida/a-florida-man-says-his-pregnant-wife-saved-his-life-in-home-invasion-with-an-ar-15/', 
    headline="A Florida man says his pregnant wife saved his life in home invasion – with an AR-15", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://www.complex.com/life/2018/11/florida-man-wearing-cros-leaps-into-crocodile-pit', 
    headline="Florida Man Wearing Crocs Leaps Into Crocodile Pit", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://6abc.com/man-climbs-building-dives-into-pond-wrestles-with-crocodile-and-survives/4641551/', 
    headline="Florida man climbs building, dives into pond, wrestles with crocodile, and survives", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='http://www.thesmokinggun.com/documents/florida/ben-dover-arrest-490172', 
    headline="Cops Bust Man Who Said Name Was 'Ben Dover'", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://patch.com/florida/miami/florida-man-makes-himself-snack-while-robbing-taco-bell', 
    headline="Florida Man Makes Himself A Snack While Robbing Taco Bell ", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://www.clickorlando.com/news/2017/11/10/naked-florida-man-breaks-into-home-tries-on-womans-clothes-police-say/', 
    headline="Naked Florida man breaks into home, tries on woman's clothes, police say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://www.mysuncoast.com/video/2019/11/11/florida-man-sues-madonna/', 
    headline="Florida man sues Madonna", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://www.tampabay.com/news/publicsafety/naked-florida-man-revealed-on-video-sneaking-into-restaurant-and-munching-on-ramen-20181112/', 
    headline="Naked Florida man revealed on video sneaking into restaurant and munching on ramen", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://www.wctv.tv/content/news/Florida-man-accused-of-killing-man-after-losing-card-game-564865302.html', 
    headline="Florida man accused of killing man after losing card game", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://abc7ny.com/4690382/', 
    headline="Police: Man dresses as woman, buys puppy with stolen credit card", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://spacedoutradio.com/florida-man-tells-police-bag-of-cocaine-they-found-in-car-must-have-blown-in-from-the-wind/', 
    headline="Florida Man Tells Police Bag Of Cocaine They Found In Car Must Have Blown In From The Wind", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://www.miamiherald.com/news/local/crime/article221780125.html', 
    headline="Florida man steals vending machine", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://wsvn.com/news/local/police-florida-man-left-2-kids-in-car-while-in-strip-club/', 
    headline="Police: Florida man left 2 kids in car while in strip club", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://www.nbc-2.com/story/39567762/florida-man-loses-his-shorts-while-breaking-into-a-car-dealership', 
    headline="Florida man loses his shorts while breaking into a car dealership", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://www.fox4now.com/news/state/florida-man-arrested-for-having-sex-with-miniature-horse-on-multiple-occasions-deputies-say', 
    headline="Florida man arrested for having sex with miniature horse on multiple occasions, deputies say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://www.mysuncoast.com/2019/11/20/florida-man-accused-fatally-beating-uncles-dog-with-shovel/', 
    headline="Florida man accused of fatally beating uncle’s dog with a shovel", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://www.wwnytv.com/2019/11/22/florida-man-demands-less-money-during-bank-robbery-deputies-say/', 
    headline="Florida man demands less money during bank robbery, deputies say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://www.wctv.tv/content/news/Florida-man-crashes-car-to-highlight-dangerous-intersection-459303423.html', 
    headline="Florida man crashes car to highlight dangerous intersection", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://www.cbsnews.com/news/video-florida-man-runs-over-own-leg-with-truck-after-leaving-strip-club/', 
    headline="Fla. man runs over own leg with truck after leaving strip club", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://www.foxnews.com/us/florida-man-tried-to-break-into-car-filled-with-cops-officials-say', 
    headline="Florida man tried to break into car filled with cops, officials say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://thetakeout.com/florida-man-stole-footlong-sandwich-pants-1831173405', 
    headline="Cops: Florida man stole footlong sandwich in his pants", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://www.bradenton.com/news/local/crime/article222198385.html', 
    headline="Florida man charged with stabbing a woman with a fork over underdone potato", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://www.abcactionnews.com/news/state/deputies-florida-man-spends-birthday-in-jail-after-intentionally-cutting-the-tails-off-of-5-kittens', 
    headline="Deputies: Florida man spends birthday in jail after intentionally cutting the tails off of 5 kittens", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://www.abcactionnews.com/news/state/florida-man-arrested-twice-this-month-for-bringing-loaded-gun-to-airport', 
    headline="Florida man arrested twice this month for bringing loaded gun to airport", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://abc30.com/4797865/', 
    headline="Suspect caught on camera with pants down during Florida car dealership burglary", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='https://www.usnews.com/news/best-states/florida/articles/2019-11-28/man-guilty-of-biting-police-officer', 
    headline="Man Guilty of Biting Police Officer", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

print("November added to database!")
print("Adding December to database...")

tmp = December(
    link='https://www.wtxl.com/news/police-florida-man-worried-about-vampires-intentionally-burns-down-his/article_da37be2c-093c-11e9-b150-1b29f7dd112f.html', 
    headline="Police: Florida man worried about vampires intentionally burns down his home", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://www.orlandoweekly.com/Blogs/archives/2016/12/02/florida-man-breaks-into-neighbors-home-to-pet-thier-cat', 
    headline="Florida man breaks into neighbor's home to pet their cat ", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='http://www.thesmokinggun.com/buster/florida/hamburger-hooker-287593', 
    headline="Florida Man Arrested After Offering Undercover Cop A Hamburger In Exchange For Sex Act", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://www.mysuncoast.com/2019/12/04/florida-man-abandons-son-highway-because-he-thinks-boy-is-gay-police-say/', 
    headline="Florida man abandons son on highway because he thinks boy is gay, police say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://www.kxxv.com/story/39610879/florida-man-arrested-for-shoplifting-after-job-interview', 
    headline="Florida man arrested for shoplifting after job interview", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://abc11.com/family/man-recovering-from-paralysis-stands-for-first-time-to-propose/4847991/', 
    headline="Florida man recovering from paralysis stands for first time during marriage proposal", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://bangordailynews.com/2018/12/18/news/nation/police-florida-man-tried-to-pay-for-mcdonalds-with-bag-of-weed/', 
    headline="Police: Florida man tried to pay for McDonald’s with bag of weed", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://www.esquire.com/news-politics/news/a40288/florida-man-naked-3-women-cadillac/', 
    headline="Florida Man Arrested After Driving 110 MPH While Naked with 3 Women in a Cadillac", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://www.nbcmiami.com/news/local/florida-man-steals-elderly-womans-purse-runs-her-over-in-mcdonalds-parking-lot/136320/', 
    headline="Florida Man Steals Elderly Woman’s Purse, Runs Her Over in McDonald’s Parking Lot ", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://www.theolympian.com/news/nation-world/national/article223086725.html', 
    headline="Man tries to escape police by jumping head-first through window", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://www.thedrive.com/news/25407/florida-man-arrested-for-dui-while-lemur-and-wallaby-escape-from-truck-during-traffic-stop', 
    headline="Florida Man Arrested for DUI While Lemur and Wallaby Escape from Truck During Traffic Stop", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://eu.pnj.com/story/news/2018/12/12/naked-florida-man-crossbow-who-claimed-aliens-were-after-him-shot-deputy/2292792002/', 
    headline="Deputy cleared for shooting naked man armed with crossbow who claimed aliens were after him ", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://www.upi.com/Odd_News/2018/12/13/Deputies-find-suspected-burglar-was-deer-trapped-in-bathroom/4181544730120/', 
    headline="Deer gets trapped in Florida man's bathroom", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://www.wctv.tv/content/news/Florida-man-arrested-for-biting-boys-out-of-frustration-502803021.html', 
    headline="Florida man arrested for biting boys out of frustration", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://www.miamiherald.com/news/state/florida/article225491760.html', 
    headline="Florida man kills in-laws after posing as their murdered daughter for a year, cops say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://www.wctv.tv/content/news/Video-Florida-man-drops-stolen-TV-from-getaway-scooter-503606471.html', 
    headline="Florida man drops stolen TV from getaway scooter", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://www.washingtontimes.com/news/2019/dec/17/florida-man-gets-prison-for-capturing-selling-wood/', 
    headline="Florida man gets prison for capturing, selling wood turtles", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://www.wctv.tv/content/news/Florida-man-pays-electric-bills-of-families-about-to-lose-power-for-Christmas-566304871.html', 
    headline="Florida man pays electric bills of families about to lose power for Christmas", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://www.wftv.com/news/local/florida-man-kicked-out-window-pulled-himself-out-of-moving-patrol-car-deputies-say/891344342/', 
    headline="Florida man kicked out window, hurled himself out of moving patrol car, deputies say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://6abc.com/florida-man-drags-police-officer-for-half-mile/2802388/', 
    headline="Florida man drags police officer for half-mile", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://www.fox13news.com/news/florida-man-becomes-upset-over-cigarette-prices-brings-loaded-rifle-into-store-officials-say', 
    headline="Florida man becomes upset over cigarette prices, brings loaded rifle into store, officials say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://www.thenewstribune.com/news/nation-world/national/article191312259.html', 
    headline="The clams this diner ordered were ‘so small’ that he called 911 — twice, police say", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://wsvn.com/news/local/police-florida-man-arrested-for-passing-out-marijuana-because-it-was-christmas/', 
    headline="Police: Florida man arrested for passing out marijuana ‘because it was Christmas’", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://eu.floridatoday.com/story/news/local/2015/12/24/time-traveling-florida-man-crashes-car-building/77897760/', 
    headline="‘Time traveling’ Florida man crashes car into building ", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://www.wctv.tv/content/news/Police-Florida-man-in-Santa-hat-stole-baby-Jesus-figurine-from-nativity-scene-on-Christmas-467911623.html', 
    headline="Police: Florida man in Santa hat stole baby Jesus figurine from nativity scene on Christmas", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://www.foxnews.com/us/florida-man-arrested-after-punching-atm-for-giving-him-too-much-money', 
    headline="Florida man arrested after punching ATM for 'giving him too much money'", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://www.fox13news.com/news/florida-man-pretends-to-be-homeless-gives-100-to-those-who-tried-to-help', 
    headline="Florida man pretends to be homeless, gives $100 to those who tried to help", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://abc6onyourside.com/news/nation-world/florida-man-charged-with-dui-says-gps-led-him-onto-railroad-tracks', 
    headline="Florida man charged with DUI says GPS led him onto railroad tracks", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://www.10news.com/news/national/florida-man-arrested-for-rigging-door-to-electrocute-pregnant-wife', 
    headline="Florida man arrested for rigging door to electrocute pregnant wife", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://www.hawaiinewsnow.com/2018/12/31/florida-man-locks-keys-car-keep-cops-searching-it/', 
    headline="Florida man locks keys in car to keep cops from searching it", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='https://nypost.com/2019/12/31/florida-man-blows-hand-off-after-lighting-firework-in-truck/', 
    headline="Florida man blows hand off after lighting firework in truck", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

print("December added to database!")
print("Database populated successfully!")
