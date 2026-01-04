# 빌드 및 실행

Kiwipet을 빌드하고 실행합니다.

## 작업 순서

1. 실행 중인 Kiwipet 프로세스 종료
2. PyInstaller로 빌드
3. 빌드된 exe 실행
4. 빌드 결과 요약 보고

```bash
# 프로세스 종료
powershell -Command "Stop-Process -Name 'Kiwipet' -Force -ErrorAction SilentlyContinue"

# 빌드
py -m PyInstaller --clean Kiwipet.spec

# 실행
start "" "dist\Kiwipet.exe"
```
