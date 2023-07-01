#include <iostream>
#include <map>

using namespace std;
char findTheDifference(string, string) ;

int main()
{
	string s = "a";
	string t = "aa";
	cout << findTheDifference(s, t) << endl;
}

char findTheDifference(string s, string t) 
{
	int str = 0;

	for (int i = 0; i < t.length(); ++i)
	{
		str += t[i];
		str -= s[i];

	}


	return char(str); 

}