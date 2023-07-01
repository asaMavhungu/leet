#include <iostream>
#include <vector>

using namespace std;

bool isAnagram(string, string ); 

int main()
{

	string s = "nl";
	string t = "cx";
	cout << isAnagram(s, t)  << endl;
}

bool isAnagram(string s, string t) 
{

	if (s.length() != t.length())
		return false;

	vector<int> arr(26, 0);

	for (int i = 0; i < s.length(); ++i)
	{
		++arr[s[i] - 'a'] ;
		--arr[t[i] - 'a'] ;
	}

	for (int i = 0; i < 26; ++i)
	{
		cout << arr[i] << endl;
	}

	cout << "dsa" << endl;
	

	for (int i = 0; i < 26; ++i)
	{
		if (arr[i] != 0)
			return false;
	}

	for (int i = 0; i < t.length(); ++i)
	{
		cout << arr[i] << endl;
	}
	

	return true;


}