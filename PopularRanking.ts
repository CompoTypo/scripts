let num_students: number = 5;
let num_options: number = 6;

// let table = new Array<number[]>(num_students)
// for (let i = 0; i < table.length; i++) {
//     table[i] = new Array<number>(num_options)
// }

let table: number[][] = [
    [31, 23, 12, 14, 28, 27],
    [31, 12, 27, 23, 1, 41],
    [23, 27, 35, 31, 12, 40],
    [23, 27, 31, 12, 41, 1],
    [31, 23, 12, 27, 1, 41]
]

function getLeftMost(table: number[][]) {
    let leftMost: number[] = [];
    for (let i = 0; i < table.length; i++) {
        leftMost.push(table[i][0])
    }
    return leftMost
}

function countBest(left_most: number[]) {
    let multi_counter: number[] = [];
    let unique_vals: number[] = [];
    let cont_flag: boolean = false;
    for (let i = 0; i < left_most.length; i++) {
        for (let j = 0; j < unique_vals.length; j++) {
            if (left_most[i] === unique_vals[j]) {
                multi_counter[j]++;
                cont_flag = true;
                break;
            }
        }
        if (!cont_flag) {
            cont_flag = false;
            continue;
        }
        unique_vals.push(left_most[i]);
        multi_counter.push(1)
    }

    let max = 0, max_i = 0;
    for (let i = 0; i < multi_counter.length; i++) {
        if (multi_counter[i] > max) {
            max = multi_counter[i];
            max_i = i;
        }
    }
    return unique_vals[max_i];
}

function clearValue(table: number[][], val: number) {
    for (let r_num = 0; r_num < table.length; r_num++) {
        for (let c_num = 0; c_num < table[r_num].length; c_num++) {
            if (table[r_num][c_num] === val) {
                table[r_num].splice(c_num, 1);
            }
        }
    }
    return table;
}

function calcBestOptions(table: number[][]) {
    let ranking: number[] = new Array<number>(num_options);
    for (let i = 0; i < ranking.length; i++) {
        let lmost: number[] = getLeftMost(table);
        let nextbest: number = countBest(lmost);
        ranking[i] = nextbest;
        clearValue(table, nextbest);
        const element = ranking[i];
    }
    return ranking;
}

console.log(calcBestOptions(table))