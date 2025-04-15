
#include <limits.h>   // INT_MAX, LONG_MIN 等

名称|	类型|  值|  用途
|---|---|---|---|
INT_MAX|	int|	2147483647|	最大 int 值
INT_MIN|	int|	-2147483648|	最小 int 值
LONG_MAX|	long|	9223372036854775807|	最大 long 值
LONG_MIN|	long|	-9223372036854775808|	最小 long 值
UINT_MAX|	unsigned|	4294967295|	最大无符号 int



名称|	类型|	说明
|---|---|---|
FLT_MAX|	float|	最大 float 值
FLT_MIN|	float|	最小正 float 值（不是负数）
DBL_MAX|	double|	最大 double 值
DBL_MIN|	double|	最小正 double 值

INT_MIN / INT_MAX 是 int 类型 → 小心溢出

LONG_MIN / LONG_MAX 是 long 类型 → 在树题中更安全

如果你需要更大的范围（比如处理 2^63），用 long long 并配 LLONG_MIN / LLONG_MAX（from <limits.h>）