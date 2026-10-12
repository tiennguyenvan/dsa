using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Result
{
    public static int binSearch(List<int> arr, long offset)
    {
        int left = 0, right = arr.Count;

        while (left < right)
        {
            int mid = left + (right - left) / 2;

            if (arr[mid] < -offset)
            {
                left = mid + 1;
            }
            else
            {
                right = mid;
            }
        }

        return left;
    }

    public static List<long> playingWithNumbers(
        List<int> arr, List<int> queries)
    {
        int n = arr.Count;
        arr.Sort();

        List<long> prefix = new List<long>();
        long cur = 0;
        prefix.Add(cur);

        for (int i = 0; i < n; i++)
        {
            cur += arr[i];
            prefix.Add(cur);
        }

        List<long> ret = new List<long>();
        long offset = 0;

        foreach (int q in queries)
        {
            offset += q;

            int k = binSearch(arr, offset);

            long left = -(prefix[k] + (long)k * offset);
            long right = prefix[n] - prefix[k]
                       + (long)(n - k) * offset;

            ret.Add(left + right);
        }

        return ret;
    }
}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(
            Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int n = Convert.ToInt32(Console.ReadLine().Trim());

        List<int> arr = Console.ReadLine()
            .TrimEnd()
            .Split(' ')
            .Select(int.Parse)
            .ToList();

        int q = Convert.ToInt32(Console.ReadLine().Trim());

        List<int> queries = Console.ReadLine()
            .TrimEnd()
            .Split(' ')
            .Select(int.Parse)
            .ToList();

        List<long> result = Result.playingWithNumbers(arr, queries);

        textWriter.WriteLine(string.Join("\n", result));

        textWriter.Flush();
        textWriter.Close();
    }
}