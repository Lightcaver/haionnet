$sourcePaths = @(
    "C:\Users\고객지원팀5\Desktop\업무자료\월간 리포팅\내꺼\제브\24.05\SG135_서버용\방화벽",
    "C:\Users\고객지원팀5\Desktop\업무자료\월간 리포팅\내꺼\제브\24.05\SG135_서버용\WAF",
    "C:\Users\고객지원팀5\Desktop\업무자료\월간 리포팅\내꺼\제브\24.05\SG105_본사\방화벽"
)

foreach ($sourcePath in $sourcePaths) {
    $files = Get-ChildItem -Path $sourcePath -Filter "reverseproxy-*"
    foreach ($file in $files) {
        $date = Get-Date $file.Name.Substring(13, 10)
        $newName = $date.ToString("yyMMdd")
        Rename-Item $file.FullName -NewName ("$newName" + ".xlsx")
    }
}