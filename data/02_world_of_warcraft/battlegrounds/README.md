# About Dataset

## Context
World of Warcraft is a MMORPG (massively multiplayer online role-playing game) video game created by Blizzard. It has a lot of content, but in this dataset we are just focusing in player vs player content.

Battlegrounds are scenarios where the two playable factions of the game (Horde and Alliance) fight against each other to win. Some of them are capture the flag them, others are take control points them, some of them are gain resources them, and some of them are a mixture of several themes. Playing battlegrounds means a lot of fun, but you we will get a currency in game called "Honor", which can be traded for powerful gear of our characters. If you wish to know more about this, you can visit the official website.

## Content
In this dataset you will find five files with the statistics at the end of each battleground. Common statistics (columns) in all files are:

- Code: code for the battleground (not needed for analysis).
- Faction: faction of the player (Horde or Alliance).
- Class: class of the player (warrior, paladin, hunter, rogue, priest, death knight, shaman, mage, warlock, monk, druid, demon hunter).
- KB: number of mortal kills given by the player.
- D: number of times that the player died.
- HK: number of killings where the player or his/her group contributed.
- DD: damage done by the player.
- HD: healing done by the player.
- Honor: honor awarded to the player.
- Win: 1 if the player won.
- Lose: 1 if the player lost.
- Rol: dps if the player is a damage dealer; heal if the player is focused in healing allies. Note that not all classes can be healers, just shaman, paladin, priest, monk and druid, but all classes can be damage dealers.
- BE: some weeks there is a bonus event, when the honor gained is increased. 1 if the battleground happened during that week.

These columns, plus the "battleground" column are in wowbgs.csv file. Battleground column represent the kind of battleground:

- AB: Arathi basin.
- BG: Battle for Gilneas.
- DG: Deepwind gorge.
- ES: Eye of the storm.
- SA: Strand of the ancients.
- SM: Silvershard mines.
- SS: Seething shore.
- TK: Temple of Kotmogu.
- TP: Twin peaks.
- WG: Warsong gulch.

The other files have statistics for just one kind of bg, and have additional columns:

- wowgil.csv: statistics for Battle for Gilneas battleground. BA: number of bases assaulted by the player. BD: number of bases defended by the player.
- wowsm.csv: statistics for Silvershard mines battleground. CC: number of carts controlled by the player.
- wowtk.csv: statistics for Temple of Kotmogu battleground: OP: number of orb controlled by the player. VP: victory points earned by the player.
- wowwg.csv: statistics for Warsong gulch battleground: FC: number of flag captured by the player. FR: number of flags defended by the player.

- In Version 2, files are the same but with a "2" in the name. You can find 1657 aditional rows and one new battleground, called Seething shore (SS). Next version will come with the new expansion of the game, Battle for Azeroth (14-8-2018), where Strand of the Ancients battleground will be no longer available and damage and healing will be reduce for all players.

Time is not important in this dataset, but the rows are ordered by the moment I collected the data, from March 2017 to January 2018. Players can improve their gear, so maybe there is a increasing factor in Damage done and Healing done over the time.

## Acknowledgements

All data was collected by me playing battlegrounds, and the name of the players will remain anonymous.

## Inspiration

With this dataset you can check which class is the lethalest, which one dies more often, which faction win more scenarios, how capturing one flag can affect the honor awarded, which class are the best at doing damage or healing, which classes have better combination in order to win each battleground and what is the chance of winning for every class, for example.