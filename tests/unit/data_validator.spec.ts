import { pokemonData10 } from '@/data/gen1_0'
import { pokemonData11 } from '@/data/gen1_1'
import { pokemonData20 } from '@/data/gen2_0'
import { pokemonData30 } from '@/data/gen3_0'
import { pokemonData40 } from '@/data/gen4_0'
import { pokemonData50 } from '@/data/gen5_0'
import { pokemonData60 } from '@/data/gen6_0'
import { pokemonData70 } from '@/data/gen7_0'
import { pokemonData80 } from '@/data/gen8_0'
import { gamePoints, gameLocations } from '@/data/reborn'


describe('pokemonData', () => {
  it('references valid values from gameLocations', () => {
    const pokemonData = pokemonData10.concat((pokemonData11 as any), (pokemonData20 as any), (pokemonData30 as any), (pokemonData40 as any), (pokemonData50 as any), (pokemonData60 as any), (pokemonData70 as any), (pokemonData80 as any))
    for (let i = 0; i < pokemonData.length; i++) {
      for (let j = 0; j < (pokemonData[i].locations ? pokemonData[i].locations!.length : 0); j++) {
        expect(gameLocations).toContain(pokemonData[i].locations![j].location)
      }
    }
  })
})

describe('pokemonData', () => {
  it('references valid values from gamePoints', () => {
    const pokemonData = pokemonData10.concat((pokemonData11 as any), (pokemonData20 as any), (pokemonData30 as any), (pokemonData40 as any), (pokemonData50 as any), (pokemonData60 as any), (pokemonData70 as any), (pokemonData80 as any))
    const gmPoints = gamePoints.map(key => key["name"])
    for (let i = 0; i < pokemonData.length; i++) {
      for (let j = 0; j < (pokemonData[i].locations ? pokemonData[i].locations!.length : 0); j++) {
        expect(gmPoints).toContain(pokemonData[i].locations![j].point)
      }
    }
  })
})
