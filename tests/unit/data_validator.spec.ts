import { pokemonData10 } from "@/data/gen1_0";
import { pokemonData11 } from "@/data/gen1_1";
import { pokemonData12 } from "@/data/gen1_2";
import { pokemonData20 } from "@/data/gen2_0";
import { pokemonData21 } from "@/data/gen2_1";
import { pokemonData30 } from "@/data/gen3_0";
import { pokemonData31 } from "@/data/gen3_1";
import { pokemonData32 } from "@/data/gen3_2";
import { pokemonData40 } from "@/data/gen4_0";
import { pokemonData41 } from "@/data/gen4_1";
import { pokemonData50 } from "@/data/gen5_0";
import { pokemonData51 } from "@/data/gen5_1";
import { pokemonData52 } from "@/data/gen5_2";
import { pokemonData60 } from "@/data/gen6_0";
import { pokemonData61 } from "@/data/gen6_1";
import { pokemonData70 } from "@/data/gen7_0";
import { pokemonData71 } from "@/data/gen7_1";
import { gamePoints, gameLocations } from "@/data/reborn";

describe("pokemonData", () => {
  it("references valid values from gameLocations", () => {
    const pokemonData = pokemonData10.concat(
      pokemonData11 as any,
      pokemonData12 as any,
      pokemonData20 as any,
      pokemonData21 as any,
      pokemonData30 as any,
      pokemonData31 as any,
      pokemonData32 as any,
      pokemonData40 as any,
      pokemonData41 as any,
      pokemonData50 as any,
      pokemonData51 as any,
      pokemonData52 as any,
      pokemonData60 as any,
      pokemonData61 as any,
      pokemonData70 as any,
      pokemonData71 as any
    );
    for (let i = 0; i < pokemonData.length; i++) {
      for (
        let j = 0;
        j < (pokemonData[i].locations ? pokemonData[i].locations!.length : 0);
        j++
      ) {
        //console.log(pokemonData[i].name + " - " + j);
        expect(gameLocations).toContain(pokemonData[i].locations![j].location);
      }
    }
  });
});

describe("pokemonData", () => {
  it("references valid values from gamePoints", () => {
    const pokemonData = pokemonData10.concat(
      pokemonData11 as any,
      pokemonData12 as any,
      pokemonData20 as any,
      pokemonData21 as any,
      pokemonData30 as any,
      pokemonData31 as any,
      pokemonData32 as any,
      pokemonData40 as any,
      pokemonData41 as any,
      pokemonData50 as any,
      pokemonData51 as any,
      pokemonData52 as any,
      pokemonData60 as any,
      pokemonData61 as any,
      pokemonData70 as any,
      pokemonData71 as any
    );
    const gmPoints = gamePoints.map((key) => key["name"]);
    for (let i = 0; i < pokemonData.length; i++) {
      for (
        let j = 0;
        j < (pokemonData[i].locations ? pokemonData[i].locations!.length : 0);
        j++
      ) {
        expect(gmPoints).toContain(pokemonData[i].locations![j].point);
      }
    }
  });
});
