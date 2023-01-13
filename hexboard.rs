fn main() {

    let rows: i8 = 13;
    let cols: i8 = 13;

    let first_piece = String::from("><");
    let second_piece = String::from("()");

    let mut row_start: i8 = rows;
    let mut col_start: i8 = 0;

    let mut row_end: i8 = rows;
    let mut col_end: i8 = 1;

    println!();
    for _ in 0..rows-1 {
        print!("   ");
    }
    println!(" {} __ {}", first_piece, second_piece);

    for _ in 0..rows+cols {
        if row_start > 0 {

            if row_start-1 > 0 {
                for _ in 0..row_start-2 {
                    print!("   ");
                }
                //print!(" {}  __", (65+row_start-2) as u8 as char);
		print!(" {} __", first_piece); 
            } else {
                for _ in 0..row_start {
                    print!("   ");
                }
            }

            if !(col_end <= cols) {
                print!("/");
            }

            row_start = row_start-1;

        } else {

            if col_start > 0 {
                for _ in 0..col_start-1 {
                    print!("   ");
                }
                print!(" {}   \\__", format!("{: <2}", col_start));
            } else {
                for _ in 0..col_start {
                    print!("   ");
                }
                print!("   \\__");
            }

            if !(col_end <= cols) {
                print!("/");
            }

            col_start = col_start+1;
        }

        if col_end <= cols {

            for loop_index in col_start..col_end {

                let _: i8 = if row_start <= 0 {
                    loop_index-col_start
                } else {
                    loop_index+row_start
                };

                let _: i8 = loop_index;

                // Print pieces from game board . . .
                //print!("/{}{}\\", (65+row_index) as u8 as char, (65+col_index) as u8 as char);
                print!("/  \\");

                if loop_index < cols-1 {
                    print!("__");
                }
            }

            if col_end != cols {
                print!(" {}", second_piece);
            }

            col_end = col_end+1;

        } else {

            let cell_end: i8 = if row_end-1 > cols {
                cols
            } else {
                row_end-1
            };

            for _ in 0..cell_end {

                //let row_index: i8 = loop_index+row_start;
                //let col_index: i8 = loop_index+col_start;

                // Print pieces from game board . . .
                //print!("{}{}\\__/", (65+row_index) as u8 as char, (65+col_index) as u8 as char);
                print!("  \\__/");
            }

            if row_end != rows {
                print!("   {}", format!("{: >2}", (65+row_end) as u8 as char));
            }

            row_end = row_end-1;
        }
        
        println!();
    }

    for _ in 0..cols-1 {
        print!("   ");
    }
    println!(" {}    {}", format!("{: <2}", cols), format!("{: >2}", (65) as u8 as char));
}
