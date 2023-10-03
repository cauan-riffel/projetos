#include <iostream>
#include <string>

using namespace std;



bool isNum(string v){
	for(char c:v){
		if(c!='0'&&c!='1'&&c!='2'&&c!='3'&&c!='4'&&c!='5'&&c!='6'&&c!='7'&&c!='8'&&c!='9'){
			return 0;
		}
	}
	return 1;
}

int main(){
	double media=-1;
	bool go=true;
	int scores=0;
	string temp;
	while(media==-1){
		cout<<"Write an note: ";
		cin>>temp;
		cout<<"\n";
		if(isNum(temp)&&stod(temp)>=0&&stod(temp)<=10){
			media=stod(temp);
			scores++;
		}
		else cout<<"Invalid value\n";
	}

	do{
		cout<<"Write an note: ";
		cin>>temp;
		cout<<"\n";
		if(temp!="break"&&isNum(temp)&&stod(temp)>=0&&stod(temp)<=10){
			scores++;
			media+=stod(temp);
			cout<<stod(temp);
		}
		else if(temp=="break"){
			break;
		}
		else cout<<"Invalid value\n";
	}while(go);

	cout<<"The media of this student is "<<media/scores<<"\n";


	return 0;
}
