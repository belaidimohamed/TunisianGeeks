#include <stdlib.h>
#include <time.h>
#include <iostream>
#include <fstream>
#include <string.h>
#include <Windows.h>
#include <cstdlib>
#include "player.h"
#include "wheel.h"
using namespace std;
class game{
	private:
	//	bool verif;
		char letter ;
		Player p1;  // instance of the first player 
		Player p2;  // instance of the second player
		Wheel w;   //instance of class wheel
		int x;  
	//	int h;
		bool roundOver ;
		string hint; //
		//int k;
		string phrase;
		string hiddenPhrase;
		string name;
		int choix;
	public:
	
int random(int a, int b){ //retourne un nombre aleatoire entre les valeurs a et b
	srand(time(NULL));
	return (rand() %b)+ a;
}

	
	void getHintPhrase(int k){
	ifstream f1 ("phrases.txt");
	string phrase;
	string hint;
	for(int j=1;j<=k;j++){
		getline(f1,phrase);
		}
		this->phrase=phrase;

	ifstream f2 ("hints.txt");
		for(int j=1;j<=k;j++){
		getline(f2,hint);
		}
		this->hint=hint;
		//cout<<this->phrase;
		this->hiddenPhrase=hidePhrase(); 
	}

	
string hidePhrase() {
	int i;
    string ch1="" ;
	for(i=0;i<phrase.length(); i++) {
	if(phrase[i]== ' ') { 
		ch1+=' ';  }
	else{
	ch1+='#' ; }} /* hidding the line (prize) by # */
	return(ch1);}
	
bool VerifPhrase() {
	bool guess ;
	//char guessed_phrase[100] ;
	//cout<< phrase ;
	string guessed_phrase;
	cin.ignore();
	cout<<"guess the phrase"<<"\n";
	getline(cin,guessed_phrase);
	
	//cout<<guessed_phrase;
	if(guessed_phrase==phrase) {
	cout<<"congratulations, you guessed right!!" ;
	guess= true;}
	else{
	cout<<"wrong phrase"<<"\n" ;
	guess= false ;}
	return guess;
	
}
void changePlayer(){
	if (name==p1.getName()){
		name=p2.getName();
	}
	else if (name==p2.getName()){
		name=p1.getName();
	}
}
string randomPlayer(){
	int i;
	string name;
	i=random(1,2);
	//cout<<i;
	//cout<<p1.getName();
	if (i==1){name=p1.getName() ;
	}
	else{
		name=p2.getName();}
		return name;
	}
	int chooseLetterOrPhrase(){
		int cc;
		cout<<"if u want to guess a phrase write 1"<<"\n"<<"if u want to guess a letter write 2"<<"\n" ;
		cin>>cc;
		this->choix=cc;
		return choix;
	}
	bool VerifLetter() {
	
	int m=false;
	cout<<" >> Select a letter : "<<"\n" ;
            cin>>letter;
            
            for(int i=0 ;i<phrase.length();i++) { // if the selected lettre is in the phrase , it will unhidden in the hidden phrase
               if(phrase[i]==letter){
               	m=true;
               	
                  if(hiddenPhrase[i]=='#'){
                     hiddenPhrase[i] =letter;
                     
                     //changePlayer() ; 
                  }
               }
               
            }
			if (m==true){
			cout<<"\n"<<" The puzzle become : "<<hiddenPhrase;}
            
            
            else if(m==false){
            	cout<<"The letter is not in the phrase !";
               //print_With_Color("\n The letter is not in the phrase !  ",12);
               //Sleep(2000);
               //system ("CLS");
               } 
			   return m; }
            
            void chooseWinner(){
            	if (p1.getScore()>p2.getScore()){
            		cout<<"\n"<<"congratulations  "<<p1.getName()<< " you won   " <<p1.getScore()<<"    $" ;
				}
				else{
            		cout<<"\n"<<"congratulations  "<<p2.getName()<< " you won  " <<p2.getScore()<<"   $" ;
				}
				}
            	
			
int play() { 

//vvhhbool verif;
 			string nameONE,nameTWO;
 			int m,choix,h;
	cout<<"donner le nom du joueur 1"<<"\n";
	cin>>nameONE;
	p1.setName(nameONE);
	cout<<"donner le nom du joueur 2"<<"\n";
	cin>>nameTWO;
	p2.setName(nameTWO);
	cout<<"le nom du joueur 1 est : "<<p1.getName()<<"\n";
	cout<<"le nom du joueur 1 est : "<<p2.getName()<<"\n";

	
	
	
	//cout<<"name is"<<name;

//	cout <<"k ="<<k;
	for (int j=1;j<=2;j++){
		this->name= randomPlayer();
		int k; // this is the the index of hint's and phrase's line in the text file 
		k=random(1,6); //here k is generated randomly ;
	
			//cout <<"k ="<<k;
		cout<<"\n"<<"-----------------------------------------round  "<<j<<"  begin ! ----------------------------------------"<<"\n";
		getHintPhrase(k);
	cout<<"the hint is : "<<hint<<"\n";
	cout<<"this is the puzzle : "<<hidePhrase()<<"\n";
	cout<<"phrase is: "<<phrase<<"\n";

	roundOver=false ;
		while(!roundOver){
			cout<<"player  "<<name<<"  is playing  "<<"\n";
			choix=chooseLetterOrPhrase();
		//	cout<<"vous avez choisi "<<choix<<"\n";
			switch (choix){
			//cout<<"choix est"<<choix;
			case 1 :                                           
				cout<<"player "<<name<<"try to guess the phrase"<<"\n";
				// cout<<VerifPhrase();
				if (VerifPhrase()){
					
					if (name==p1.getName()){
						p1.updateScore(10000);
					}
					else if (name==p2.getName()){
						p2.updateScore(10000) ;}
						roundOver=true;}
				else{
					changePlayer(); 
				}
						break;
					
		    case 2 :
				cout<<"player  "<<name<<"   try to guess a letter"<<"\n";
				if (VerifLetter()) {
					if (hiddenPhrase==phrase){
						cout<<" congratulations ! you solved the puzzle!!"<<"\n";
						roundOver=true;
					}
					m= w.calculatePointsLetter(letter,phrase);
					if (name==p1.getName()){
						p1.updateScore(m);}
				    else if (name==p2.getName()){
						p2.updateScore(m) ;}
						}
					
				else {
					changePlayer();
				}
				break;
				
				 
			default :
				cout<<"choice incorrect please choose 1 or 2"<<"\n" ;
				break;
					}}	}
		
	chooseWinner(); //choose the winner at the end of the second round
	}
	
 };
	int main(){
		game g;
		
	
	cout<<g.play()<<"\n" ;
	
	
}
