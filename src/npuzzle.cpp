#include <iostream>
#include <fstream>
#include <string>
#include "puzzle.h"

#define COMMENT_CHAR '#'

#define ISSPACE(c) (c == ' ' || c == '\t')
#define ISSPACENL(c) (c == ' ' || c == '\t' || c == '\n')

int *parseFile(char *av)
{
	ifstream f;
	string line;

	f.open(av);
	if (f.is_open())
	{
		while(getline(f, line))
		{
			int i = 0;
			while (i < line.size())
			{
				
			}
		}
	}
	cout << endl;
}

int main(int argc, char **argv)
{
	Puzzle *myPuzzle = new Puzzle(atoi(argv[1]));
	parseFile(argv[1]);

	myPuzzle->setGoal();
	myPuzzle->printGoal();
	return 0;
}
