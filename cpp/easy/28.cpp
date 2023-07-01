#include <iostream>


using namespace std;


int strStr(string, string) ;



int main()
{
	string haystack = "mississippi";
	string needle = "issip";
	
	cout << strStr(haystack, needle) << endl;
}

int strStr(string haystack, string needle) 
{

	int hayInd = 0;
	int nedInd = 0;

	int nedSize = needle.length();

	for (int i = 0; i < haystack.length(); ++i)
	{

		cout << haystack[i] << " " << i << " " << needle[nedInd] << " "  << nedInd << endl;

		if (haystack[i] == needle[nedInd])
		{

			//cout << haystack[i] << " " << i << " " << needle[nedInd]  << endl;

			++nedInd;

			if (nedInd == nedSize)
				return i + 1 - nedSize;
		}

		else 
		{
			i -= nedInd;
			nedInd = 0;
		}

		

	}
	
	return -1;
}