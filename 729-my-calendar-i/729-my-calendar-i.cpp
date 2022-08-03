#define vi vector<int>
class MyCalendar {
public:
    map<vi, bool> pq;
    MyCalendar() {
    }
    
    bool book(int start, int end) {
        for(auto it =pq.begin(); it!=pq.end(); it++){
            if(start>=it->first[0] && start<it->first[1]) return false;
            if(end>it->first[0] && end<=it->first[1]) return false;
            if(start<=it->first[0] && end>=it->first[1]) return false;
        }
        pq[{start, end}]=true;
        return true;
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(start,end);
 */