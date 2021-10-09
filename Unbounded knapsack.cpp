/*In this multiple occurences of same item are allowed
*/
#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define pll pair<ll, ll>
#define vl vector<ll>
#define pb push_back
#define f(i, a, b) for (ll i = a; i < b; ++i)
#define rev(i, a, b) for (ll i = a; i >= b; --i)
#define print(x) cout << x << endl
#define endl '\n'
#define F first
#define S second
#define setbits(x) __builtin_popcountll(x)
#define zerobits(x) __builtin_ctzll(x)
#define to(n) to_string(n)
#define low(v, n) lower_bound(v.begin(), v.end(), n) - v.begin()
#define upp(v, n) upper_bound(v.begin(), v.end(), n) - v.begin()
#define mod 1000000007
#define mex 100005

ll knap(ll weight[], ll value[], ll n, ll W)
{
    ll dp[n + 1][W + 1];
    memset(dp, 0, sizeof(dp));
    //base conditions are same

    f(i, 1, n + 1)
    {
        f(j, 1, W + 1)
        {
            if (weight[i - 1] > j)
            {
                dp[i][j] = dp[i - 1][j];
            }
            else
            {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - weight[i - 1]] + value[i - 1]); //now we can include as many times so we don't decrease size of array
            }
        }
    }

    return dp[n][W];
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    ll n, W;
    cin >> n >> W;
    ll weight[n];
    ll value[n];
    f(i, 0, n)
    {
        cin >> weight[i];
    }
    f(i, 0, n)
    {
        cin >> value[i];
    }

    print(knap(weight, value, n, W));
    return 0;
}