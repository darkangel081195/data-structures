#include<iostream>

int main(){
    int n,k;//n-> Total items in the house// k->The weight of knapsack
    std::cin>>n>>k;
    int itm[n],wt[n],value[n];//itm->number of the item,wt->weight of ith item,value->value of ith iterm
    int res[n][k];//resultant table
    int remain=0;
    for(int i=0;i<n;i++){
        std::cin>>itm[i]>>wt[i]>>value[i];
    }

    for(int j=0;j<k;j++){
        if(wt[0] > j+1){
            res[0][j] = 0;
        }
        else{
            res[0][j] = value[0];
        }
    }


    for(int i=1;i<n;i++){
        for(int j=0;j<k;j++){
            if(wt[i] > j+1){
                res[i][j] = res[i-1][j];
                continue;
            }
            remain = (j+1) - wt[i];
            if(remain > 0){
                remain = res[i-1][remain-1];
            }
            else{
                remain = 0;
            }
            res[i][j] = std::max(res[i-1][j],(value[i]+remain));
        }
    }

    std::cout<<res[n-1][k-1];
//Uncomment below lines to see how the table is filled.
    // for(int i=0;i<n;i++){
    //     for(int  j=0;j<k;j++){
    //         std::cout<<res[i][j]<<' ';
    //     }
    //     std::cout<<"\n";
    // }

    return 0;
}

// Input:
// 3 4
// 1 4 3000
// 2 3 2000
// 3 1 1500
// Output:
// 3500
