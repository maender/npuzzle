#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Puzzle
{
public:
	Puzzle(unsigned int sz);
	~Puzzle();
	int **getGoal();
	void setGoal();
	void printGoal();

private:
	unsigned int _size;
	int **_goal;
};