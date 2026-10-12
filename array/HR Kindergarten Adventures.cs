using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Solution {

    /*
     * Complete the solve function below.
     */
    static int solve(int[] t) {
        /*
         * Return the ID
         */
         int n = t.Length;
         int[] bad = new int [n+1];
         
         for (var i = 0; i < n; i++) {
            if (t[i] == 0) continue;
            if (t[1] >= n) {
                bad[0] += 1;
                bad[n] -= 1;
                continue;
            }
            var start = (i - t[i] + 1 + n) % n;
            var end = i+1;
            bad[start] += 1;
            bad[end] -= 1;
            if (start > end) {
                bad[n] -= 1;
                bad[0] += 1;                
            }            
         }                  
         
         int min = int.MaxValue;
         int failures = 0;
         int bestIndex = 0;
         for (var i = 0; i < n; i++) {
            failures += bad[i];
            if (failures < min) {
                min = failures;
                bestIndex = i;
            }
         }
         
         return bestIndex + 1;
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int tCount = Convert.ToInt32(Console.ReadLine());

        int[] t = Array.ConvertAll(Console.ReadLine().Split(' '), tTemp => Convert.ToInt32(tTemp))
        ;
        int id = solve(t);

        textWriter.WriteLine(id);

        textWriter.Flush();
        textWriter.Close();
    }
}
