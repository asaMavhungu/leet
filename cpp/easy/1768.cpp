#include <iostream>
#include <string>
using namespace std;

string mergeAlternately(string , string ) ;


int main()
{
	//cout << "hello" << endl;

	string word1 = "ab"; 
	string word2 = "pqrs";

	string ans = mergeAlternately(word1, word2);

	cout << ans << endl;
	
	return 0;
}


string mergeAlternately(string word1, string word2) 
{
	string str ("");

	int size1 = word1.length() < word2.length() ? word1.length() : word2.length();
	int size2 = word1.length() > word2.length() ? word1.length() : word2.length();

	string * cpy = word1.length() > word2.length() ? &word1 : &word2;



	for (int i = 0; i < size1; ++i)
	{
		str += word1[i];
		str += word2[i];
	}



	cout << cpy[1] << endl;

	for (int i = size1; i < size2; ++i)
	{
		str += (*cpy)[i];
	}


	return str;

}