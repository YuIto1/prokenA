import math
from scipy.stats import norm

def calc_odds_ratio_and_ci(a, b, c, d, alpha=0.05):
    """
    2x2のクロス集計表の値からオッズ比と信頼区間を計算する関数

    入力:
      a: ExposureありかつOutcomeあり
      b: ExposureありかつOutcomeなし
      c: ExposureなしかつOutcomeあり
      d: ExposureなしかつOutcomeなし
      alpha: 有意水準 (デフォルト0.05)

    出力:
      オッズ比, 信頼区間下限, 信頼区間上限
    """
    # オッズ比
    or_value = (a * d) / (b * c)

    # オッズ比の対数の標準誤差
    se_log_or = math.sqrt(1/a + 1/b + 1/c + 1/d)

    # z値（片側alpha/2）
    z = norm.ppf(1 - alpha/2)

    # 信頼区間（対数オッズ比の範囲）
    log_or = math.log(or_value)
    ci_lower = math.exp(log_or - z * se_log_or)
    ci_upper = math.exp(log_or + z * se_log_or)

    return or_value, ci_lower, ci_upper

if __name__ == "__main__":

    a = int(input("ExposureありOutcomeありの個数:"))
    b = int(input("ExposureありOutcomeなしの個数:"))
    c = int(input("ExposureなしOutcomeありの個数:"))
    d = int(input("ExposureなしOutcomeなしの個数:"))

    or_val, ci_low, ci_up = calc_odds_ratio_and_ci(a, b, c, d)
    print(f"オッズ比: {or_val:.3f}")
    print(f"95%信頼区間: [{ci_low:.3f}, {ci_up:.3f}]")
