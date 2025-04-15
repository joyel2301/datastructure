/*
인덱스 i번째 값 출력하기
정수 n을 입력받아 입력받은 n 만큼 한 개의 배열에 정수를 저장하세요.
그리고, 배열의 특정 인덱스를 의미하는 수 i를 입력 받아 배열의 i번째 값을 출력하는 프로그램을 작성하세요.

입력
첫 번째 줄에서는 한 개의 배열에서 입력을 받는 개수를 나타내는 정수 n(1 <= n <= 1000)을 입력받습니다. 두 번째 줄에서는 배열에 들어가는 n개의 정수들이 입력이 됩니다. 세 번째 줄에서는 배열의 인덱스 정수 i(0 <= i < n)을 입력받습니다. 이때 입력되는 정수들은 정수의 범위를 초과하지 않습니다.

출력
출력 형식은 Sample Output과 같은 형식을 따릅니다. 배열 인덱스 i에 들어있는 정수 값을 출력하고, 출력이 끝나면 개행처리를 해줍니다.
*/
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n; 

    vector<int> arr(n); 


    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    int index;
    cin >> index; 


    cout << arr[index] << endl;

    return 0;
}
