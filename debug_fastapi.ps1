$env:PYTHONPATH = "c:\Users\NIKIT\Desktop\tinyfish;$env:PYTHONPATH"
$proc = Start-Process ".\venv\Scripts\python.exe" -ArgumentList "-m", "uvicorn", "app.main:app", "--port", "8001" -PassThru -NoNewWindow -RedirectStandardError "uvicorn_err.log" -RedirectStandardOutput "uvicorn_out.log"
Start-Sleep -Seconds 3
Invoke-RestMethod -Uri "http://127.0.0.1:8001/agent/run?url=https://example.com" -ErrorAction SilentlyContinue 
Start-Sleep -Seconds 1
Stop-Process -Id $proc.Id -Force
Get-Content uvicorn_err.log
