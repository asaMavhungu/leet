#include <iostream>
#include <string>
#include <cstdint>


using namespace std;

int test()
{

	string asa;
	cout << "Hello ";
	cin >> asa;

	cout << "hello " << asa << " " << stoi("5") << endl; 



	const int numRows = 3;
    const int numCols = 4;

	int** twoDArray = new int*[numRows];


	// Create and insert arrays into the 2D array
    for (int i = 0; i < numRows; i++) {
        twoDArray[i] = new int[numCols];
        for (int j = 0; j < numCols; j++) {
            twoDArray[i][j] = i * numCols + j + 1; // Insert values sequentially
        }
    }

	    // Access elements using the pointer notation
    int value = twoDArray[1][3]; // Access A[1][2]

    // Print the value
    std::cout << "A[1][2] = " << value << std::endl;

	return 0;


}


int binary_sqrt(int input_num)
{

	int hi = input_num;
	int lo = 0;
	int mid = lo + (hi-lo+1)/2;


	while (hi>lo)
	{
		if (mid > input_num / mid)
		{
			hi = mid -1;
		}
		else
		{
			lo = mid;
		}


		mid = (hi+lo+1)/2;
	}

	return lo;


}


int main()
{

	string input_str;


	//cin >> input_str;

	int num = 99;//stoi(input_str);

	cout << binary_sqrt(num) << endl;

	return 0;

}