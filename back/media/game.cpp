#include <stdio.h>
#include <iostream>
#include <fstream>

#include <Windows.h> // this  is used to color the texts
#include <stdlib.h> // this used for cin.getline() function
#include <cstdlib> // this  is used fr time sleeping
#include "decorating.h"
#include "play.h"

using namespace std;

/*--------------------------------------------------------  Functions ------------------------------------------------------*/
string GotoLine(ifstream& myfile , int num) {
  string line;
  int x=0;
  if (myfile.is_open())
    while ( getline (myfile,line) )
    { x++;
      if(x==num)
        {myfile.close();
        return line ;}
    }
    myfile.close();
}
/*--------------------------------------------------------- Declarations ---------------------------------------------------------------------*/

int main() {
   decorating color ;
   srand(time(NULL));; //call it once to generate random number

   string ask1,ask2,hint;
   int x = 0 ;
   string language = "English" ;// id of the choosed lang
   int k = 0; // variable to altern between players (p1 then p2 , p1 then p2 ...)
   char guess[200];  // guess for the phrase by the players
   bool gameover = false; // check if the game over or not (the game is over if the phrase is completely exposed , and still no one figure it out)
   string ch1 ,ch;
   int num;


/*----------------------------------------------------------- réglages and signing up ----------------------------------------------------*/
   color.welcome();
   while(x!=1 && x!=2 && x!=3){
      try{
         color.title("--",0,"");
         cout<<" select a language : \n  1) french  \n  2) english  \n";
         cin>>x;
         system ("CLS"); /* clear screen */
      }
      catch (const std::exception&)
      {
         cout<<"c'est n'est pas un nombre -_- !";
      }

   }

   if(x==1){
      language = "French";
      ask1= "Donner le nom du 1er joueur :  ";
      ask2=" Donner le nom du 2eme joueur : ";

   }
   if(x==2){
      language = "English";
      ask1= "Player 1 please enter your name : ";
      ask2= " Player 2 please enter your name : ";
   }



   color.title(language,0,"");
   // adding players
   Player* p1 = new Player  ;
   Player* p2 = new Player ;
   char y[50];
   color.print_With_Color(ask1,11);
   cin.ignore();
   cin.getline(y,50);
   p1->setName(y);
   color.print_With_Color(ask2,11);
   cin.getline(y,50);
   p2->setName(y);




/*-------------------------------------------------------- main game code ---------------------------------------------------------------*/


   for(int i=1 ; i<4 ; i++){
      Sleep(2000);
      system ("CLS");
      num=rand()%3 +1;    // get a random number between 0-9 (index of array)
      ch1 = "" ; // variable in which will store the hidden phrase
      num=i; // delete that line if u want to have random phraszs
      if (language=="French"){
         ifstream file("french_phrases.txt");
         ifstream file2("french_hints.txt");
         ch = GotoLine(file,num);
         hint = GotoLine(file2,num);
         }
      else{
         ifstream file2("english_hints.txt");
         ifstream file("english_phrases.txt");
         ch = GotoLine(file,num);
         hint = GotoLine(file2,num);
      }

      for (int i = 0; i < ch.length(); i++) {ch1+='#'; } /* hidding the line (prize) by # */
      play playy(language , ch,i,hint) ;
      while(!gameover && ch1!="end"){
         if(k%2==0){
            ch1 = playy.playing(p1,p2,ch1);
         }
         else{
            ch1 = playy.playing(p2,p1,ch1);
         }
         k++;
      }}
   return 0;
/*-------------------------------------------------------- End of game --------------------------------------------------------*/
}
