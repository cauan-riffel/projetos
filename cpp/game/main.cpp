#include<iostream>
#include<string>
#include<random>

using namespace std;

//utils.h
namespace utils{
	#include<random>
	#include<string>
	int* rI(int t,int b,int q=1,bool r=true){
		random_device m;
		mt19937 gen(m());
		uniform_int_distribution dis(t,b);

		int* arr=new int[q+1];
		int c=0;
		while(c<q){
			int v=dis(gen);
			if(!r){
				bool s=true;
				for(int i=0;i<q;i++){
					if(arr[i]==v){
						s=false;
					}
				}
				if(s){
					arr[c]=v;
					c++;
				}
			}else{
				arr[c*4]=v;
				c++;
			}
		}
		arr[q]=-1;

		return arr;
	}

	bool IsInt(string s,bool hex=false){
		if(s=="9"){
			cout<<"\n";
		}
		char arr[16]={'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
		int m;
		if(hex){
			m=15;
		}else{
			m=10;
		}
		for(int i=0;i<s.size();i++){
			bool is=false;
			for(int j=0;j<m;j++){
				if(s[i]==arr[j]){
					is=true;
					break;
				}
			}
			if(!is)return false;
		}
		return true;
	}

	template <typename T>
	void cl(T* d){
		delete[] d;//Segmentation fault
	}
	void cls(string* d){
		delete d;
	}

}

class Game{
private:
	int b,p,min=0,max;
	string* a;
public:
	int steps=0;
	Game(int s){
		a=new string[s];
		max=s;
		if(s/10<5)b=s/5;
		else if(s/10<15)b=s/10;
		else b=15;
		for(int i=0;i<max;i++){
			a[i]=to_string(i+1);
		}
		p=*utils::rI(0,max);
	}

	void showArr(){
		for(int i=0;i<max;i++){
			cout<<a[i]<<"\t";
			if(!((i+1)%b))cout<<"\n";
		}
		cout<<endl;
	}

	bool canTurn(int h){
		string _=to_string(h);
		for(int i=min;i<max;i++){
			if(a[i]==_){
				return true;
			}
		}
		return false;
	}

	bool turnHouses(int h){
		steps++;
		h--;
		if(h==p)return true;
		if(h>p){
			for(int i=h;i<max;i++){
				a[i]="X";
			}
		}else{
			for(int i=h;i>=0;i--){
				a[i]="X";
			}
		}
		return false;
	}

	~Game(){
		utils::cl(a);
	}
};

int main(){
	string* temp=new string;
	cout<<"Quantos caracteres você quer em sua tabela? ";
	cin>>*temp;
	cout<<"\n";
	while(!utils::IsInt(*temp)||stoi(*temp)<=10){
		cout<<"Insira um valor superior a 10! ";
		cin>>*temp;
		cout<<"\n";
	}
	Game game(stoi(*temp));
	utils::cls(temp);

	bool discovered=false;
	while(!discovered){
		string action;
		game.showArr();
		cout<<"qual peça você quer virar? ";
		cin>>action;
		if(utils::IsInt(action)&&game.canTurn(stoi(action))){
			if(game.turnHouses(stoi(action))){
				discovered=true;
				cout<<"Peça encontrada utilizando "<<game.steps<<" passos!!!"<<"\n";
			}
		}else{
			cout<<"Valor inserido incorreto ou não pode ser acessado na tabela!"<<"\n";
		}
	}
	cout<<"\n";
	return 1;
}
