class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        vector<vector<int>> dist(m, vector<int>(n, 0));
        // cout << dist.size() << " " << dist[0].size() << "\n";
        vector<pair<int, int>> dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        queue<pair<int, int>> q;

        int answer = 0;

        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j] == 2) {
                   for (auto [dx, dy] : dirs) {
                        int x = i+dx;
                        int y = j+dy;
                        if (x >= 0 && y >= 0 && x < m && y < n && grid[x][y] == 1) {
                            q.push({i, j});
                            break;
                        }
                   }
                }
            }
        }

        while (!q.empty()) {
            auto [x, y] = q.front(); q.pop();
            cout << x << " " << y << "\n\n";

            for (auto [dx, dy] : dirs) {
                int x2 = x+dx;
                int y2 = y+dy;
                if (x2 >= 0 && y2 >= 0 && x2 < m && y2 < n && grid[x2][y2] == 1) {
                    // cout << x2 << " " << y2 << " " << "\n";
                    grid[x2][y2] = 2;
                    dist[x2][y2] = dist[x][y]+1;
                    answer = max(dist[x2][y2], answer);
                    q.push({x2, y2});
                }
            }
        }

        for (auto row : grid) {
            for (auto e : row) {
                if (e == 1) return -1;
            }
        }

        return answer;
    }
};