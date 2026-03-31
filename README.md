# TartanAir-V2

Hello and welcome to the official TartanAir repository. This repository includes a set of tools that complement the [TartanAir Dataset](https://www.tartanair.org/). 

## Setup

- Construct virtual environment and install Tartanair-V2 package locally
    ```bash
    conda create --name tartanair-v2 python=3.10
    conda activate tartanair-v2
    git clone git@github.com:Itachi6912110/Tartanair-V2.git
    cd Tartanair-V2
    git submodule update --init --recursive
    pip install -e .
    ```

## Download Datasets

- Using example download script. It will download several sequences to `datasets/Tartanair-V2`
  ```bash
  python3 examples/download_example.py
  ```

- Download the datasets used in [GMMap]().

### `ta.download()` Reference

```python
import tartanair as ta
ta.init('your/data/root')

ta.download(
    env        = ['Prison', 'Ruins'],
    difficulty = ['easy', 'hard'],
    modality   = ['image', 'depth'],
    camera_name= ['lcam_front', 'lcam_back'],
    unzip      = True,
    delete_zip = False,
    num_workers= 4,
    data_source= 'huggingface',
)

# Or via a YAML config file (all other args are ignored when config is set):
ta.download(config='examples/download_config.yaml')
```

#### Arguments

| Argument | Type | Default | Description |
|---|---|---|---|
| `env` | str or list | `[]` | Environments to download. Empty list downloads **all** environments. |
| `difficulty` | str or list | `[]` | Trajectory difficulty. Empty list downloads both. Valid: `'easy'`, `'hard'`. |
| `modality` | str or list | `[]` | Data modalities to download. Empty list downloads all. |
| `camera_name` | str or list | `[]` | Camera views to download. Empty list downloads all. Not required for `'imu'` or `'lidar'`. |
| `config` | str | `None` | Path to a YAML config file. When provided, **all other arguments are ignored**. |
| `unzip` | bool | `False` | Automatically unzip downloaded files. |
| `delete_zip` | bool | `False` | Delete zip files after unzipping. Only takes effect when `unzip=True`. |
| `num_workers` | int | `1` | Number of parallel download workers. Values >1 enable multi-threaded downloading. |
| `data_source` | str | `'huggingface'` | Download source. Options: `'huggingface'`, `'airlab'`. |

#### Valid `env` values (75 environments)

```
AbandonedCable, AbandonedFactory, AbandonedFactory2, AbandonedSchool,
AmericanDiner, AmusementPark, AncientTowns, Antiquity3D, Apocalyptic,
ArchVizTinyHouseDay, ArchVizTinyHouseNight, BrushifyMoon, CarWelding,
CastleFortress, CoalMine, ConstructionSite, CountryHouse, CyberPunkDowntown,
Cyberpunk, DesertGasStation, Downtown, EndofTheWorld, FactoryWeather, Fantasy,
ForestEnv, Gascola, GothicIsland, GreatMarsh, HQWesternSaloon, HongKong,
Hospital, House, IndustrialHangar, JapaneseAlley, JapaneseCity, MiddleEast,
ModUrbanCity, ModernCityDowntown, ModularNeighborhood, ModularNeighborhoodIntExt,
NordicHarbor, Ocean, Office, OldBrickHouseDay, OldBrickHouseNight,
OldIndustrialCity, OldScandinavia, OldTownFall, OldTownNight, OldTownSummer,
OldTownWinter, PolarSciFi, Prison, Restaurant, RetroOffice, Rome, Ruins,
SeasideTown, SeasonalForestAutumn, SeasonalForestSpring, SeasonalForestSummerNight,
SeasonalForestWinter, SeasonalForestWinterNight, Sewerage, ShoreCaves, Slaughter,
SoulCity, Supermarket, TerrainBlending, UrbanConstruction, VictorianStreet,
WaterMillDay, WaterMillNight, WesternDesertTown
```

#### Valid `modality` values

| Value | Requires `camera_name` | Notes |
|---|---|---|
| `'image'` | Yes | RGB images |
| `'depth'` | Yes | Depth maps |
| `'seg'` | Yes | Segmentation masks |
| `'flow'` | Yes — `lcam_front` only | Optical flow |
| `'event'` | Yes | Event camera data; `'easy'` difficulty only |
| `'imu'` | No | IMU measurements |
| `'lidar'` | No | LiDAR point clouds |

#### Valid `camera_name` values (16 cameras)

`lcam_*` = left camera, `rcam_*` = right camera.

```
lcam_front, lcam_left, lcam_right, lcam_back, lcam_top, lcam_bottom, lcam_fish, lcam_equirect
rcam_front, rcam_left, rcam_right, rcam_back, rcam_top, rcam_bottom, rcam_fish, rcam_equirect
```

#### Config YAML schema

```yaml
# examples/download_config.yaml
env: ['ArchVizTinyHouseDay']
difficulty: ['easy']
modality: ['image', 'depth', 'seg', 'imu']
camera_name: ['lcam_front', 'lcam_left', 'lcam_right', 'lcam_back', 'lcam_top', 'lcam_bottom', 'lcam_fish']
unzip: True
delete_zip: False
num_workers: 4
```

## Visualize Datasets

### `ta.visualize()` Reference

Interactively visualizes a locally downloaded trajectory using OpenCV windows. Press any key to advance to the next frame.

```python
import tartanair as ta
ta.init('your/data/root')

ta.visualize(
    env           = 'SoulCity',
    difficulty    = 'easy',
    trajectory_id = 'P003',
    modality      = ['image', 'depth'],
    camera_name   = ['lcam_front'],
)
```

#### Arguments

| Argument | Type | Default | Description |
|---|---|---|---|
| `env` | str or list | required | Environment name(s) to visualize. |
| `difficulty` | str or list | `['easy']` | Trajectory difficulty. Valid: `'easy'`, `'hard'`. |
| `trajectory_id` | str or list | `['P000']` | Trajectory ID(s) of the form `P000`, `P001`, etc. |
| `modality` | str or list | `[]` (all) | Modalities to display. Valid: `'image'`, `'depth'`, `'seg'`, `'flow'`. |
| `camera_name` | str or list | `[]` (all) | Camera views to display. Same valid values as `ta.download()`. |
| `show_seg_palette` | bool | `False` | Show the semantic segmentation color palette in a separate window. Requires a `seg_label_map.json` file in the environment directory. |

#### Notes

- Up to 5 images are displayed per row; additional cameras/modalities wrap to the next row.
- The frame index, camera name, and modality are overlaid on each image.
- `'flow'` modality is only available for `lcam_front`.