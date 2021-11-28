export type Move<T> = {
  [K in keyof T]: string[];
};

export interface Location {
  location: string;
  point: string;
  method: string;
}

export interface Pokemon {
  no: number;
  name: string;
  types: string[];
  stats: number[];
  levelUpMoves: Move<any>;
  eggMoves: string[];
  tmTutorMoves: string[];
  locations: Location[];
}
