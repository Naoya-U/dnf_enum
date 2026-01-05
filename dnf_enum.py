import itertools

def cube_to_minterms(cube, n):
    mins = set()
    for m in range(2 ** n):
        bits = tuple((m >> i) & 1 for i in reversed(range(n)))
        ok = True
        for cb, mb in zip(cube, bits):
            if cb is None:
                continue
            if cb != mb:
                ok = False
                break
        if ok:
            mins.add(m)
    return mins

def cube_to_string(cube):
    """cubeを文字列（例: a'b'd）に変換"""
    vars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    s = ""
    for v, val in zip(vars, cube):
        if val == 1:
            s += v
        elif val == 0:
            s += v + "'"
    return s or "1"


def format_sop(cubes):
    """複数のcubeを + でつないで1つのSOP文字列にする"""
    return " + ".join(cube_to_string(c) for c in cubes)


def is_prime_implicant(cube, minterms, n):
    """cubeが主項（prime implicant）かどうか判定"""
    covered = cube_to_minterms(cube, n)
    if not covered or not covered <= minterms:
        return False

    # 変数を1つNoneにしてもまだ valid なら、cubeは極大でない
    for i in range(n):
        if cube[i] is not None:
            generalized = list(cube)
            generalized[i] = None
            gen_cov = cube_to_minterms(tuple(generalized), n)
            if gen_cov <= minterms:
                return False
    return True


def generate_all_cubes(n):
    """4変数の全cube（3^4通り）を生成"""
    vals = [0, 1, None]
    return list(itertools.product(vals, repeat=n))


def generate_irredundant_sops(minterms, n):
    """主項のみを使って、全非冗長積和形を列挙"""
    all_cubes = generate_all_cubes(n)

    # 主項（prime implicant）のみ抽出
    prime_cubes = [c for c in all_cubes if is_prime_implicant(c, minterms, n)]

    # 各主項がカバーするミンターン
    cube_cover = {c: cube_to_minterms(c, n) for c in prime_cubes}

    irredundant_forms = []
    for r in range(1, len(prime_cubes) + 1):
        for combo in itertools.combinations(prime_cubes, r):
            union_cover = set().union(*(cube_cover[c] for c in combo))
            if union_cover == minterms:
                # 冗長性チェック
                redundant = False
                for i in range(len(combo)):
                    smaller = combo[:i] + combo[i+1:]
                    small_cover = set().union(*(cube_cover[c] for c in smaller))
                    if small_cover == minterms:
                        redundant = True
                        break
                if not redundant:
                    irredundant_forms.append(combo)
    return irredundant_forms

def count_literals_in_cube(cube):
    """1積項内のリテラル数を返す"""
    return sum(1 for val in cube if val is not None)

def total_literals_in_sop(cubes):
    """積和形全体のリテラル総数"""
    return sum(count_literals_in_cube(c) for c in cubes)

n = int(input("変数の個数を入力: "))

f_id = input("出力を順に入力: ")
truth = list(map(int, f_id))
minterms = {i for i, val in enumerate(truth) if val == 1}



forms = generate_irredundant_sops(minterms, n)

for form in forms:
    print(format_sop(form))