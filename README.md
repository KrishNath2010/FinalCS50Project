# KRINIKA-WORDLE
#### Video Demo:  https://www.youtube.com/watch?v=dz3ETvHel9U
#### Description: 
The goal of my game is to guess an English word that has between 4 to 8 letters. The player will choose how many letters are in the word they want to guess, and the computer will pick the word randomly. Now, the player guesses the word within 6 attempts to win the game. 

The reason I made KRINIKA-WORDLE was when I played Wordle it was fun but I wanted to do words with a different amount of letters, not just 5. And thats why I decided to give user an option to choose between 4 to 8 letters.

Also, once I played it, I had to wait for one more day to play another one. My game randomly chooses a word every time, so you can play as many times as you want in the day. This version is not like different versions of wordle because it is not a website. 

Since my vocabulary was not that good, I had trouble finding the word even If I had many clues, so in KRINIKA-WORDLE you can choose the amount of letters and there is a option that you can put in letters and it will tell you all words that have those letters and are possible as the hidden word. This helps the game become easier if the player needs any help.

4letterwords.txt contains all 4 letter words. 
5letterwords.txt contains all 5 letter words. 
6letterwords.txt contains all 6 letter words. 
7letterwords.txt contains all 7 letter words. 
8letterwords.txt contains all 8 letter words. 
wordle.py is the program, the main piece is the function wordle that does all calculations and does everything except the first 5-10 prints, The order of the function is n*m with m being the number of words that have n letters, and n being the numbers of letters in a word that the user put as input. All my code is contained in it too, the other txt files are just words. 

A big choice I also made was to use python and not c because it is easier to code in python and I am more familiar with it. 

Another choice I made was that I use minus for black and not yellow. I thought of this because minus means negative , for yellow I did pipe because it is straight, green is plus because green is good.

The reason I displayed color is because in wordle there is color  and since mine is not a website I wanted to have some visual things. The reason I put a letter list is because you can see all letters that can help you combine them to make them words. 

I did not display which letters are not used because it was sort of covered in the letter list I had been talking about. 

A big improvement I could make is to make my project a website.
