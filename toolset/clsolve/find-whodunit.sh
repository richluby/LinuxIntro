#!/bin/bash

#grep -i clue crimescene
# CLUE: Found a wallet believed to belong to the killer: no ID, just loose change, and membership cards for AAA, Delta SkyMiles, the local library, and the Museum of Bash History. The cards are totally untraceable and have no name, for some reason.

memberList=$(comm -12 <(comm -12 <(sort memberships/Terminal_City_Library) <(sort memberships/Museum_of_Bash_History)) <(comm -12 <(sort memberships/AAA) <(sort memberships/Delta_SkyMiles)))

#CLUE: Questioned the barista at the local coffee shop. He said a woman left right before they heard the shots. The name on her latte was Annabel, she had blond spiky hair and a New Zealand accent.

#grep -i annabel people
#head -n 40 streets/Hart_Place | tail -n 1
#etc... 
#Annabel's
#SEE INTERVIEW #47246024
#SEE INTERVIEW #699607	<-- WINNER WINNER CHICKEN DINNER
#SEE INTERVIEW #871877
#SEE INTERVIEW #9437737

#INTERVIEW #699607
#Interviewed Ms. Church at 2:04 pm.  Witness stated that she did not see anyone she could identify as the shooter, that she ran away as soon as the shots were fired.

#However, she reports seeing the car that fled the scene.  Describes it as a blue Honda, with a license plate that starts with "L337" and ends with "9"

vehiclesList=$(grep -A 3 'L337.*9' vehicles | grep -i -A 2 "Honda" | grep -i -A 1 "Blue" | grep -i Owner | cut -d ' ' -f2,3|sort)


bothlist=$(comm -12 <(echo "$vehiclesList") <(echo "$memberList"))

echo "$bothlist"


