# Good Python Conventions
## name_main.py
왜 우리가 `def main`, `if __name__ == '__main__':`을 사용해야 되는지.
```py
    def main():
        print("Hello World")
    
    if __name__ == '__main__': 
        main()
```
### 모듈에 대한 정보 전달
 - 코드를 보는 다른 사람은 해당 스크립트를 보고 모듈이 실행할 수 있는 모듈인지, 아니면 그저 다른 파일에 `import`될 모듈인지 인지 가능하다
### 의도치 않은 실행 방지
 - `if dunder name == dunder main`이 없는 파일은 `import`가 되면 실행이 되면서 사용이 된다. 이것을 방지해준다.
### main() 까지 정의를 해주는 이유
 - `main()`이 없이 단지 `if __name__ == '__main__':` 만 사용하면, 해당 코드 블록에 있는 변수는 `global`로 정의가 된다. 
 - 따라서 이로인해 생기는 다양한 문제가 있기 때문에 `main()` 함수를 정의 후 `if __name__ == '__main__':` 에서 호출해주는 것이다.