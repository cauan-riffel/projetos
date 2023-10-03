#include<iostream>
#include<string>
#include<map>
#include<vector>

using namespace std;

class Word{
private:
	string s,ss="";
	int l;
	static map<char,vector<char>>m;

	void changeWord(char w){
		for(int i=0;i<l;i++){
			if(s[i]==w){
				ss[i]=w;
			}
		}
	}

public:
	Word(string str){
		s=str;
		l=str.length();
		for(char c:str){
			if(c!=' '||c!='-'){
				ss+="_";
			}else ss+=c;
		}
	};
	string getString(){
		return ss;
	}
	bool correctWord(char c){
		if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||c=='c'){
			bool t=0;

		}
		for(char i:s){
			if(i==c){
				changeWord(c);
				return true;
			}
		}
		return false;
	}
};

map<char,vector<char>>Word::m={
		{'c',{'c','ç'}},
		{'a',{'a','ã','â','á','à'}},
		{'e',{'e','é','ê'}},
		{'i',{'i','í'}},
		{'o',{'o','ó','õ'}},
		{'u',{'u','ú'}}
	};

int main(){
	cout<<"ç"<<endl;
	Word game("paulinho da hornet");
	cout<<game.getString()<<endl;
	cout<<game.correctWord('a')<<endl;
	cout<<game.getString();



	cout<<"\n";
	return 0;
}
