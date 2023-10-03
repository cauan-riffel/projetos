#include<iostream>
#include<string>
#include<random>

using namespace std;

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
			arr[c]=v;
			c++;
		}
	}
	arr[q]=-1;

	return arr;
}


template <typename T>
void cl(T* d) {
    delete[] d;
}

class Game{
private:
	int l,b;
	string* a;
public:
	Game(int s){
		a=new string[s];
		l=s;
		if(s/10<15)b=s/10;
		else b=15;
		for(int i=0;i<l;i++){
			a[i]=to_string(i+1);
		}
	}

	void showArr(){
		for(int i=0;i<l;i++){
			cout<<a[i]<<'\t';
			if(!((i+1)%b))cout<<'\n';
		}
	}


	~Game(){
		cl(a);
	}
};


int main(){
	if(false){
		int* temp=new int;
		cout<<"Quantos caracteres você quer em sua tabela? ";
		cin>>*temp;
		Game game(*temp);
		cl(temp);
		game.showArr();
		cout<<'\n';
	}else{
		int* t=rI(0,50,25,false);
		int x=0;
		while(true){
			cout<<t[x];
			if(t[x]==-1){
				break;
			}
			x++;
		}
		cl(t);
	}
	return 1;
}
