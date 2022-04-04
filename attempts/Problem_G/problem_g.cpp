#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
using namespace std;
int main()
{
   string filename = "money.txt";
   bool success = true;
   ifstream inFile;
   int n, cust, numF, numT, numTw, input, myTotal;
   inFile.open(filename);
   inFile >> n;
   numF=numT=numTw=myTotal=0;
   for (int start = 0; start<n; start++)
   {
      inFile >> cust;
      for (int customer=0; customer<cust; customer++)
      {
         inFile >> input;
         if (input == 5)
         {
            numF++;
         }
         else if(input == 10)
         {
            numT++;
            numF--;
            if(numF < 0)
               success = false;
         }
         else if (input == 20)
         {
            numTw++;
            if (numT >= 1)
            {
               numT--;
               numF--;
               if(numF < 0)
                  success = false;
            }
            else
            {
               numF--;
               numF--;
               numF--;
               if(numF < 0)
                  success = false;
            }
         }
         if (numF < 0 || numT < 0 || numTw < 0)
            success = false;
         //cout << "Current Fives: " << numF << " Current Tens: " << numT << " Current 20s: " << numTw << endl;
      }//Loop
      if (success == true)
         cout << "true" << endl;
      else
         cout << "false" << endl;
      numF=numT=numTw=0;
      success = true;
   }
   inFile.close();
}
