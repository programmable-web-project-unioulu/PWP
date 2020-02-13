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
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = July(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

print("July added to database!")
print("Adding August to database...")

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = August(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

print("August added to database!")
print("Adding September to database...")

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = September(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

print("September added to database!")
print("Adding October to database...")

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = October(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

print("October added to database!")
print("Adding November to database...")

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = November(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

print("November added to database!")
print("Adding December to database...")

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

tmp = December(
    link='', 
    headline="", 
    modtime=datetime.now()
)
db.session.add(tmp)
db.session.commit()

print("December added to database!")
print("Database populated successfully!")
