#include <iostream>
#include <gtest/gtest.h>

using namespace std;    
int addTwoNum(int x,int y){
    return x+y;
}TEST(myTests, addTwoNumReturnsInt)
{
    int result {0};                
    result = addTwoNum(10, 22);    
    GTEST_ASSERT_EQ(result, 32);   
}


int sum(int a, int b){
    int result = a + b;
    return result;
}
int main(int argc, char const *argv[])
{
    // cout<<sum(2, 6);
    // return 0;

    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
