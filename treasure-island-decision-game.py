{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "22878457-16e7-4e6d-9a16-db92ca6544dc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "*******************************************************************************\n",
      "          |                   |                  |                     |\n",
      " _________|________________.=\"\"_;=.______________|_____________________|_______\n",
      "|                   |  ,-\"_,=\"\"     `\"=.|                  |\n",
      "|___________________|__\"=._o`\"-._        `\"=.______________|___________________\n",
      "          |                `\"=._o`\"=._      _`\"=._                     |\n",
      " _________|_____________________:=._o \"=._.\"_.-=\"'\"=.__________________|_______\n",
      "|                   |    __.--\" , ; `\"=._o.\" ,-\"\"\"-._ \".   |\n",
      "|___________________|_._\"  ,. .` ` `` ,  `\"-._\"-._   \". '__|___________________\n",
      "          |           |o`\"=._` , \"` `; .\". ,  \"-._\"-._; ;              |\n",
      " _________|___________| ;`-.o`\"=._; .\" ` '`.\"\\ ` . \"-._ /_______________|_______\n",
      "|                   | |o ;    `\"-.o`\"=._``  '` \" ,__.--o;   |\n",
      "|___________________|_| ;     (#) `-.o `\"=.`_.--\"_o.-; ;___|___________________\n",
      "____/______/______/___|o;._    \"      `\".o|o_.--\"    ;o;____/______/______/____\n",
      "/______/______/______/_\"=._o--._        ; | ;        ; ;/______/______/______/_\n",
      "____/______/______/______/__\"=._o--._   ;o|o;     _._;o;____/______/______/____\n",
      "/______/______/______/______/____\"=._o._; | ;_.--\"o.--\"_/______/______/______/_\n",
      "____/______/______/______/______/_____\"=.o|o_.--\"\"___/______/______/______/____\n",
      "/______/______/______/______/______/______/______/______/______/______/_____ /\n",
      "*******************************************************************************\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(r'''\n",
    "*******************************************************************************\n",
    "          |                   |                  |                     |\n",
    " _________|________________.=\"\"_;=.______________|_____________________|_______\n",
    "|                   |  ,-\"_,=\"\"     `\"=.|                  |\n",
    "|___________________|__\"=._o`\"-._        `\"=.______________|___________________\n",
    "          |                `\"=._o`\"=._      _`\"=._                     |\n",
    " _________|_____________________:=._o \"=._.\"_.-=\"'\"=.__________________|_______\n",
    "|                   |    __.--\" , ; `\"=._o.\" ,-\"\"\"-._ \".   |\n",
    "|___________________|_._\"  ,. .` ` `` ,  `\"-._\"-._   \". '__|___________________\n",
    "          |           |o`\"=._` , \"` `; .\". ,  \"-._\"-._; ;              |\n",
    " _________|___________| ;`-.o`\"=._; .\" ` '`.\"\\ ` . \"-._ /_______________|_______\n",
    "|                   | |o ;    `\"-.o`\"=._``  '` \" ,__.--o;   |\n",
    "|___________________|_| ;     (#) `-.o `\"=.`_.--\"_o.-; ;___|___________________\n",
    "____/______/______/___|o;._    \"      `\".o|o_.--\"    ;o;____/______/______/____\n",
    "/______/______/______/_\"=._o--._        ; | ;        ; ;/______/______/______/_\n",
    "____/______/______/______/__\"=._o--._   ;o|o;     _._;o;____/______/______/____\n",
    "/______/______/______/______/____\"=._o._; | ;_.--\"o.--\"_/______/______/______/_\n",
    "____/______/______/______/______/_____\"=.o|o_.--\"\"___/______/______/______/____\n",
    "/______/______/______/______/______/______/______/______/______/______/_____ /\n",
    "*******************************************************************************\n",
    "''')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "96b0effb-695b-4a6a-b531-23f42d29299d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Treasure Island.\n",
      "Your mission is to find the treasure.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n",
      " right\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You fell into a hole. Game Over.\n"
     ]
    }
   ],
   "source": [
    "print(\"Welcome to Treasure Island.\")\n",
    "print(\"Your mission is to find the treasure.\")\n",
    "left_right = input('You\\'re at a cross road. Where do you want to go? Type \"left\" or \"right\"\\n').lower()\n",
    "if left_right == 'left':\n",
    "    print(\"You've come to a lake. There is an island in the middle of the lake.\")\n",
    "    swim_wait = input('Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\\n').lower()\n",
    "    if swim_wait == 'wait':\n",
    "        print(\"You arrive at the island unharmed. There is house with 3 doors.\")\n",
    "        red_yellow_blue = input(\"One red, one yellow and one blue. \"\n",
    "                                \"Which colour do you choose?\\n\").lower()\n",
    "        if red_yellow_blue == 'red':\n",
    "            print(\"It's a room full of fire. Game Over.\")\n",
    "        elif red_yellow_blue == 'blue':\n",
    "            print(\"You entered a room of beasts. Game Over.\")\n",
    "        elif red_yellow_blue == 'yellow':\n",
    "            print(\"You found the treasure! You Win!\")\n",
    "        else:\n",
    "            print(\"Invalid Door\")\n",
    "    elif swim_wait == 'swim':\n",
    "        print(\"You get attacked by an angry trout. Game Over.\")\n",
    "    else:\n",
    "        print(\"Invalid Action.\")\n",
    "\n",
    "elif left_right == 'right':\n",
    "    print(\"You fell into a hole. Game Over.\")\n",
    "else:\n",
    "    print(\"Invalid Direction\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
