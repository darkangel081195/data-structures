#include<iostream>
using namespace std;

// Main algorithm: in order to rotate the whole matrix, we'll just rotate one ring at a time
// We can do this in-place to achieve O(1) additional space complexity
int main() {
    int n, m, k;
    char s;
    cin>>k;
    cin>>n>>s>>m;
    int **matrix = new int*[n];
    for(int i = 0; i < n; i++) {
        matrix[i] = new int[m];
        for(int j = 0; j < m; j++) {
            cin>>matrix[i][j];
            if(j<m-1){
                cin>>s;
            }
        }
    }

    int numRings = min(n,m)/2;
    for(int i = 0; i < numRings; i++) {
        int numRotations = k%(2*(n + m - 4*i) - 4);
        if(i%2 == 0){
            //Rotate anticlockwise direction
            for(int rotation = 0; rotation < numRotations; rotation++) {
                // Rotate top row
                for(int j = i; j < m-i-1; j++) {
                    int tmp = matrix[i][j];
                    matrix[i][j] = matrix[i][j+1];
                    matrix[i][j+1] = tmp;
                }
                // Rotate right column
                for(int j = i; j < n-i-1; j++) {
                    int tmp = matrix[j][m-i-1];
                    matrix[j][m-i-1] = matrix[j+1][m-i-1];
                    matrix[j+1][m-i-1] = tmp;
                }
                // Rotate bottom row
                for(int j = m-i-1; j > i; j--) {
                    int tmp = matrix[n-i-1][j];
                    matrix[n-i-1][j] = matrix[n-i-1][j-1];
                    matrix[n-i-1][j-1] = tmp;
                }
                // Rotate left column
                for(int j = n-i-1; j > i+1; j--) {
                    int tmp = matrix[j][i];
                    matrix[j][i] = matrix[j-1][i];
                    matrix[j-1][i] = tmp;
                }
            }
        }
        else{
            //Rotate clockwise direction
            for(int rotation = 0; rotation < numRotations; rotation++) {
                //Rotate Top row
                for(int j = m-i-1; j > i; j--) {
                    int tmp = matrix[i][j];
                    matrix[i][j] = matrix[i][j-1];
                    matrix[i][j-1] = tmp;
                }
                // Rotate left column
                for(int j = i; j < n-i-1; j++) {
                    int tmp = matrix[j][i];
                    matrix[j][i] = matrix[j+1][i];
                    matrix[j+1][i] = tmp;
                }
                // Rotate bottom row
                for(int j = i; j < m-i-1; j++) {
                    int tmp = matrix[n-i-1][j];
                    matrix[n-i-1][j] = matrix[n-i-1][j+1];
                    matrix[n-i-1][j+1] = tmp;
                }
                // Rotate right column
                for(int j = n-i-1; j > i+1; j--) {
                    int tmp = matrix[j][m-i-1];
                    matrix[j][m-i-1] = matrix[j-1][m-i-1];
                    matrix[j-1][m-i-1] = tmp;
                }
            }
        }
    }
    // Output final matrix
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cout<<matrix[i][j];
            if(j<m-1){
                cout<<s;
                }
        }
        cout<<"\n";
    }
        return 0;
}
