#!/bin/bash
comm -12 <(grep -A 3 'L337.*9' vehicles | grep -i -A 2 "Honda" | grep -i -A 1 "Blue" | grep -i Owner | cut -d ' ' -f2,3|sort ) <(comm -12 <(comm -12 <(sort memberships/Terminal_City_Library) <(sort memberships/Museum_of_Bash_History)) <(comm -12 <(sort memberships/AAA) <(sort memberships/Delta_SkyMiles)))
