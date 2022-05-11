package com.mycompany.team

import com.fasterxml.jackson.databind.MapperFeature
import org.json4s.DefaultFormats
import org.json4s.JsonAST.{JNothing,JNull,JValue}

import org.joda.time.format.DateTimeFormat
import org.joda.time.{DateTime, DateTimeZone, Days, LocalDate}
import org.joda.time.format.{DateTimeFormat, DateTimeFormatter}


object HelperTools {

  //Constants
  val ROUNDING_SCALE = 2
  val MICRO_PER_DOLLAR = 1000000.0
  val ROUNDING_SCALE_DECIMALL_TO_DECIMALL = 6
  
org.json4s.jackson.JsonMethods.mapper.configure(MapperFeature.SORT_PROPERTIES_ALPHABETICALLY,true)

def doubleToDecimal(x : Option[Double]):Option[BigDecimal] = {
x match {
  case Some(x) => {
           Some(BigDecimal(x).setScale(ROUNDING_SCALE_DECIMALL_TO_DECIMALL, BigDecimal.RoundMode.HALF_UP).toDouble
        }
   case None => { None }
     }
 }
                
  
 def microsToDecimal(x: Long): BigDecimal = {
                BigDecimal( x * 1.0d / MICRO_PER_DOLLAR).setScale(ROUNDING_SCALE,BigDecimal.RoundingMode.HALF_EVEN)
 }


def microsToDecimalOption(x: Option[Long]) : Option[BigDecimal] = {
   x match {
      case Some(x) => {
      Some(BigDecimal( x * 1.0d / MICRO_PER_DOLLAR).setScale(ROUNDING_SCALE,BigDecimal.RoundingMode.HALF_EVEN))
      }
     Case None => { None }
   }

 }


def fromEpochToStringTimestamp( ts: Option[Long], format: String ): String = {
   if (ts.isEmpty) {return null}
   val millisecons = if ( ts.get < 1000 000 000 000 L ) ts.get * 1000 else ts.get
   new DateTime(milliseconds).toDateTime.withZone(DateTimeZone.UTC).toString(format)
}
                
 def fromStringToStringTimestamp(ts:String , inputFormat:String, outputFormat: String): String = {
 if (Option(ts).getOrElse("")==""){return null}
 val DATE_FORMATTER = DateTimeFormat.forPattern(inputFormat)
 val tsInput = DateTime.parse(ts,DATE_FORMATTER )
 val tsOutput = tsInput.toString(outputFormat)
 
   tsOutput
 }

 
  def objectToJsonString[T](obj : T): String = { org.json4s.JsonMethods.mapper.writeValueAsString(obj)}
                
                
 def coalesceValue(x: String , y: String): String = { if (x != "") x else y}
 def coalesceValue(x: Null , y: String ): String = { y }
 def coalesceValue(x: String , y: Null ): String = { x }               
 def coalesceValue(x: Null , y: Null): Null = { null }
 def coalesceValue[T](x: Option[T] , y: Option[T]): Option[T] = { if (x.isDefined) x else y }

}
