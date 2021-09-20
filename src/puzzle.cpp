#include "puzzle.h"

Puzzle::Puzzle(unsigned int sz)
{
	_size = sz;
	_goal = NULL;
}

Puzzle::~Puzzle()
{
	if (_goal)
	{
		for (int i = 0; i < _size; i++)
		{
			if (_goal[i])
			{
				free(_goal[i]);
				_goal[i] = NULL;
			}
		}
		free(_goal);
		_goal = NULL;
	}
}

void Puzzle::printGoal()
{
	for (int i = 0; i < _size; i++)
	{
		for (int j = 0; j < _size; j++)
		{
			if (_goal[i][j])
				printf("%3d ", _goal[i][j]);
			else
				printf("%3c ", ' ');
		}
		cout << endl;
	}
}

int **Puzzle::getGoal()
{
	return _goal;
}

void Puzzle::setGoal()
{
	int ts = _size * _size;
	int cur = 1;
	int x = 0;
	int ix = 1;
	int y = 0;
	int iy = 0;
	int puzzle[ts];

	_goal = (int**)malloc(sizeof (int*) * _size);
	for (int i = 0; i < _size; i++)
	{
		_goal[i] = (int*)malloc(sizeof (int) * _size);
		memset(_goal[i], -1, sizeof(int) * _size);
	}
	memset(puzzle, -1, sizeof(int) * ts);
	while (1)
	{
		puzzle[x + y * _size] = cur;
		if (cur == 0)
			break;
		cur += 1;
		if (x + ix == _size || x + ix < 0 || (ix != 0 && puzzle[x + ix + y*_size] != -1))
		{
			iy = ix;
			ix = 0;
		}
		else if (y + iy == _size || y + iy < 0 || (iy != 0 && puzzle[x + (y+iy)*_size] != -1))
		{
			ix = -iy;
			iy = 0;
		}
		x += ix;
		y += iy;
		if (cur == _size * _size)
			cur = 0;
	}
	for (int i = 0; i < _size; i++)
	{
		for (int j = 0; j < _size; j++)
		{
			_goal[i][j] = puzzle[i * _size + j];
		}
	}
}
