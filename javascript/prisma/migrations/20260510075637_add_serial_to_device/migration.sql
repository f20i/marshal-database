/*
  Warnings:

  - A unique constraint covering the columns `[serial]` on the table `Device` will be added. If there are existing duplicate values, this will fail.
  - Added the required column `serial` to the `Device` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "Device" ADD COLUMN     "serial" TEXT NOT NULL;

-- CreateIndex
CREATE UNIQUE INDEX "Device_serial_key" ON "Device"("serial");
