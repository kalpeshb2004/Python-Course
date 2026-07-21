# import time

# def kalu():
#     print("hello high 1")
#     time.sleep(2)
#     print("hello high 2")

# def kallu():
#     print("bye 1")
#     time.sleep(3)
#     print("bye 2")
# kalu()
# kallu()

# import asyncio

# async def ramlal():
#     print("hello ramlal")
#     await asyncio.sleep(2)
#     print("hellu tramlal")

# async def rambandhu():
#     print("rambandhu bye")
#     await asyncio.sleep(3)
#     print("jeena yaha marna yaha")

# async def main():
#     await asyncio.gather(ramlal(),rambandhu())

# asyncio.run(main())

# P1 — Easy
# Async function likh brew_tea() jo print kare "Tea banana shuru", 2 sec wait kare (asyncio.sleep), phir print kare "Tea ready". asyncio.run() se chala.

# import asyncio

# async def brew_tea():
#     print("Tea banana shuru")
#     await asyncio.sleep(2)
#     print("Tea ready")

# asyncio.run(brew_tea())

# P2 — Medium
# Do async functions bana — cook_rice() (3 sec) aur cook_dal() (2 sec). asyncio.gather() use karke dono parallel chala, aur total time print kar (~3 sec aana chahiye, 5 nahi).

import asyncio

async def cook_rice():
    print("rice is cooking")
    await asyncio.sleep(3)
    print("hello")

async def cook_daal():
    print("daal is cooking")
    await asyncio.sleep(2)
    print("bye")

async def main():
    await asyncio.gather(cook_rice(),cook_daal())

asyncio.run(main())



