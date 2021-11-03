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
  level_up_moves: Move<any>;
  egg_moves: string[];
  tm_tutor_moves: string[];
  locations: Location[];
}
