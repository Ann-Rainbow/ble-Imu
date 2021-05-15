from core_main import init, start_probe, destroy

if __name__ == '__main__':
    init()
    try:
        while True:
            n = input("Введите номер пробы: ")
            r = input("Введите результат: ")
            start_probe(n)
            with open(f'all_probes/{n}_probe/Result', 'w') as f:
                f.write(r)
    except KeyboardInterrupt:
        destroy()