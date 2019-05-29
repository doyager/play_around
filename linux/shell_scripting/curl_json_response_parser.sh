#!/bin/bash
function jsonval {
    temp=`echo $json | sed 's/\\\\\//\//g' | sed 's/[{}]//g' | awk -v k="text" '{n=split($0,a,","); for (i=1; i<=n; i++) print a[i]}' | sed 's/\"\:\"/\|/g' | sed 's/[\,]/ /g' | sed 's/\"//g' | grep -w $prop`
    echo ${temp##*|}
}

json_response=`curl -X POST \"http://hostname1.company.com:8081/portal-api/login\" -H \"accept: */*\" -H \"Content-Type: application/json\" -d \"{ \\"password\\": \”PASSWord\”, \\"username\\": \\"username1\\"}\"`

#input json for testing
json="{  \"token\": \"eyJhbGciOiJIUzUxMiJ9.eyJmaXJzdE5hbWUiOiJTcmluYXlhbiIsImxhc3ROYW1lIjoiTWFjaGFybGEgU3JpIiwic3ViIjoiQUcwMzgxMiIsInBob25lIjoiKiIsImV4cCI6MTU1OTEwMDA3NSwiaWF0IjoxNTU5MDk5MTc1LCJlbWFpbCI6InNyaW5heWFuLm1hY2hhcmxhc3JpQGFudGhlbS5jb20iLCJ0ZW5hbnQiOjEsImF1dGhvcml0aWVzIjpbInEuZHVwbGljYXRlUmV2aWV3UnVsZS53cml0ZSIsInEuaXFyLWNvc3RCYXNlZC53cml0ZSIsInEuYWRob2NSdWxlLndyaXRlIiwicS5mbHUtU2hvdFJ1bGUud3JpdGUiLCJxLmJlbmVmaXRzUnVsZS53cml0ZSIsInEubWV0cmljUXVhbnRpdHlSdWxlLndyaXRlIiwid29ya2l0ZW0ucmVhZCIsInEubWFjaGluZWxlYXJuaW5nLndyaXRlIiwibGlicmFyeS53cml0ZSIsInEuZXN0cmFkaW9sLndyaXRlIiwicS5yeGNsYWltcy53cml0ZSIsInEuZW5veGFwYXJpbi53cml0ZSIsIndvcmtpdGVtLndyaXRlIiwibGlicmFyeS5yZWFkIiwicS5lZC53cml0ZSIsImxpYnJhcnkuZXhlY3V0ZSIsImxpYnJhcnkuY29uZmlnIiwidXNlcnMucmVhZCIsInEuY3VzdG9tTmRjLndyaXRlIl19.W-3M-BKrUGAzNYak9UiKPlEH0zhVMCIat6L9h5SFmb8KoLqjTz_3cawD6diK-L7gdQxoRH7p3KBKrAUPjVOKnA\",\"success\": true}"
prop='token'
token_val=`jsonval`

echo -e "\n token val: \n"
echo $token_val

# to fire curl remove echo command 
echo -e "\n curl command: \n"
echo "curl -X POST \"http://hostname1.company.com:8081/restservice1/v1/executions\" -H \"Authorization: Bearer $token_val\" -H \"accept: */*\" -H \"Content-Type: application/json\" -d '{\"AppID\":\"2888\",\"adhoc\":true}'"
