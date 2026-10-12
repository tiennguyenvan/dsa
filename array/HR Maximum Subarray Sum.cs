using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Result
{

    /*
     * Complete the 'maximumSum' function below.
     *
     * The function is expected to return a LONG_INTEGER.
     * The function accepts following parameters:
     *  1. LONG_INTEGER_ARRAY a
     *  2. LONG_INTEGER m
     */

    public static long maximumSum(List<long> a, long m)
    {
        int n = a.Count;
        long cur = 0;
        long maxMod = 0;
        SortedSet<long> prev = [];
        for (int i = 0; i < n; i++) {
            cur = (cur + a[i]) % m;            
            maxMod = Math.Max(maxMod, cur);
            if (maxMod == m - 1) return maxMod;
            prev.Add(cur);
            
            // we don't care about smaller than cur
            // because they decrease cur
            // as we already has max = Max(max,cur)
            // so only larger than cur needed to care
            // to max (cur -  prev + m)
            // we should find the smallest prev > cur
            var view = prev.GetViewBetween(cur + 1, m - 1);
            using var it = view.GetEnumerator();
            if (it.MoveNext()) {
                var next = it.Current;
                maxMod = Math.Max(maxMod, (cur - next + m) % m);
            }
                               
        }
        return maxMod;
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int q = Convert.ToInt32(Console.ReadLine().Trim());

        for (int qItr = 0; qItr < q; qItr++)
        {
            string[] firstMultipleInput = Console.ReadLine().TrimEnd().Split(' ');

            int n = Convert.ToInt32(firstMultipleInput[0]);

            long m = Convert.ToInt64(firstMultipleInput[1]);

            List<long> a = Console.ReadLine().TrimEnd().Split(' ').ToList().Select(aTemp => Convert.ToInt64(aTemp)).ToList();

            long result = Result.maximumSum(a, m);

            textWriter.WriteLine(result);
        }

        textWriter.Flush();
        textWriter.Close();
    }
}