package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
)

/*
 * Complete the solve function below.
 */
func solve(t []int32) int32 {
    /*
     * Return the ID
     */
    n := len(t)
    bad := make([]int32, n+1)
    
    for i:=0; i<n; i++ {
        if t[i] == 0 {
            continue
        }
        if t[i] >= int32(n) {
            bad[0] += 1
            bad[n] -= 1
            continue
        }
        
        start := (int32(i) - t[i] + 1 + int32(n)) % int32(n)
        end := int32(i) + 1
        bad[start] += 1
        bad[end] -= 1
        if start > end {
            bad[n] -= 1
            bad[0] += 1
        }                        
    }
    
    minFails := int32(n + 1)
    fails := int32(0)
    bestI := 0
    for i:=0; i < n; i++ {
        fails += bad[i]
        if fails >= minFails {
            continue
        }
        minFails = fails
        bestI = i
    }
    return int32(bestI) + 1
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 1024 * 1024)

    tCount, err := strconv.ParseInt(readLine(reader), 10, 64)
    checkError(err)

    tTemp := strings.Split(readLine(reader), " ")

    var t []int32

    for tItr := 0; tItr < int(tCount); tItr++ {
        tItemTemp, err := strconv.ParseInt(tTemp[tItr], 10, 64)
        checkError(err)
        tItem := int32(tItemTemp)
        t = append(t, tItem)
    }

    id := solve(t)

    fmt.Fprintf(writer, "%d\n", id)

    writer.Flush()
}

func readLine(reader *bufio.Reader) string {
    str, _, err := reader.ReadLine()
    if err == io.EOF {
        return ""
    }

    return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
    if err != nil {
        panic(err)
    }
}
